/**
 * @copyright Maichong Software Ltd. 2016 http://maichong.it
 * @date 2016-11-24
 * @author Liang <liang@maichong.it>
 */

'use strict';

var fs = require('fs');
var archiver = require('archiver');

module.exports = function (file, options) {
  var ext = file.match(/\w+$/)[0] || file;
  var output = fs.createWriteStream(file);
  var archive = archiver(ext, options);
  var done;
  var error;
  var promise;
  var onSuccess;
  var onError;

  output.on('close', function () {
    done = true;
    if (onSuccess) {
      onSuccess();
    }
  });

  // good practice to catch this error explicitly
  archive.on('error', function (err) {
    error = err;
    if (onError) {
      onError(err);
    }
    throw err;
  });

  // pipe archive data to the file
  archive.pipe(output);

  let finalize = archive.finalize;
  archive.finalize = function () {
    if (error) return Promise.reject(error);
    if (done) return Promise.resolve();
    if (!promise) {
      promise = new Promise(function (resolve, reject) {
        onSuccess = resolve;
        onError = reject;
      });
      finalize.call(archive);
    }
    return promise;
  };

  return archive;
};

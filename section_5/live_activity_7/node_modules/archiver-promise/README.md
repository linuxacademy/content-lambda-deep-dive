# archiver-promise

Promise wrapper for archiver

```js

var archiver = require('archiver-promise');

var archive = archiver('path/to/file.zip',{
  store: true
  // more options https://archiverjs.com/docs/
});

// append a file from stream
var file1 = __dirname + '/file1.txt';
archive.append(fs.createReadStream(file1), { name: 'file1.txt' });

// append a file from string
archive.append('string cheese!', { name: 'file2.txt' });

// append a file from buffer
var buffer3 = new Buffer('buff it!');
archive.append(buffer3, { name: 'file3.txt' });

// append a file
archive.file('file1.txt', { name: 'file4.txt' });

// append files from a directory
archive.directory('subdir/');

// append files from a glob pattern
archive.glob('subdir/*.txt');

// finalize the archive
archive.finalize().then(function(){
  console.log('done');
});

```

// Here is where we load the SDK for JavaScript
const AWS = require('aws-sdk');

// We need to set the region.
AWS.config.update({region: 'us-east-1'});

// Creating S3 service object
const s3 = new AWS.S3({apiVersion: '2006-03-01'});

exports.handler = (event, context, callback) => {
    // Here we list all S3 Buckets
    s3.listBuckets(function(err, data) {
       if (err) {
          console.log("Error:", err);
       } else {
          console.log("List of all S3 Buckets", data.Buckets);
       }
    });
};
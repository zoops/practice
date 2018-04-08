const https = require('https'),
  http = require('http'),
  fs = require('fs'),
  path = require('path');

let url = 'http://github.com/ParkDyel/ParkDyel.github.io/blob/master/static/image/profile.jpg?raw=true';
let dest = '.' + path.sep + 'output.jpg';
var protocol;

let downloadCb = (m) => {
  if (m.type != "info") {
    console.log(m);
  } else {
    // console.log(m);
    console.log('Done. save ' + m.url + ' to ' + m.dest);
  }
  return;
}

let download = (urls, dests, cb) => {
  let files = [];
  urls.forEach((e, idx, array) => {
    let url = urls[idx];
    let dest = dests[idx];
    console.log('Start save url ' + url + ' to ' + dest);
    files[idx] = fs.createWriteStream(dest);
    console.log("URL Protocol is " + url.split(':')[0]);
    protocol = ((url.split(':')[0]) == 'http' ? http : https);
    // console.log(protocol);
    console.log("Set Protocol as " + protocol);
    let req = protocol.get(url, (res) => {
      res.pipe(files[idx]);
      files[idx].on('finish', function () {
        let info = {
          type: "info",
          url: url,
          dest: dest
        }
        files[idx].close(cb(
          info
        )); // close() is async, call cb after close completes.
      });
    }).on('error', function (err) { // Handle errors
      fs.unlink(dest); // Delete the file async. (But we don't check the result)
      if (cb) {
        cb(err.message);
      }
    });
  });

  return;
};

let main = () => {
  let urls = [];
  let dests = [];
  if (process.argv.length > 2) {
    urls.push(process.argv[2]);
    dests.push(url.split('/').pop());
  }
  for (let idx = 1; idx < 100; idx++) {
    let url = "http://imgcomic.naver.net/webtoon/651617/153/20180331002013_31b475420a30a2d72e28f34575f26b32_IMAG01_" + idx + ".jpg";
    let dest = url.split('/').pop(); //dest = 'output.' + url.split('.').pop()
    urls.push(url);
    dests.push(dest);
    console.log('Set url ' + url + ' as ' + dest);
  }
  download(urls, dests, downloadCb);
  return 0;
}

main();
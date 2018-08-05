const me = "Miner: ";
const nkn = require('nkn-client');
const sha256 = require('sha256');

// const client = nkn();
const client = nkn({
    identifier: 'id0',
    privateKey: '2'
});

const id1 = 'id1.036b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296';
// console.log(client.key.privateKey, client.key.publicKey);
console.log(client.addr);

client.on('connect', () => {
    console.log('Connection opened.');
    client.send(id1, me + "hello")
        .then(() => {
            console.log('Received ACK');
        });
    let i = 0;
    client.on('message',
              (src, payload) =>
              {
                  if (i == 0) {
                      console.log(payload);
                      let guess = sha256(" " + 1);
                      console.log('Sending neighbor guess ' + guess);
                      client.send(src, guess);
                  } else if (i == 1) {
                      console.log('Received merkle number ' + payload);
                      let msg = me + 'working on solution...';
                      console.log('Sending: ' + msg); 
                      client.send(src, msg + ' ' + i);
                  } else {
                      client.send(src, me + 'got it ' + i);
                  }
                  i++;
              });

});


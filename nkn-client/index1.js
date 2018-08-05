const me = "Neighbor: ";
const nkn = require('nkn-client');
const sha256 = require('sha256');

// const client = nkn();
const client = nkn({
    identifier: 'id1',
    privateKey: '1'
});
console.log(client.key.privateKey, client.key.publicKey);
console.log(client.addr);

const id0 = 'id0.037cf27b188d034f7e8a52380304b51ac3c08969e277f21b35a60b48fc47669978';

client.on('connect', () => {
    console.log('Connection opened.');
    client.send(id0, me + "hello")
        .then(() => {
            console.log('Received ACK');
        });
    let i = 0;
    client.on('message',
              (src, payload) => {
                  if (i == 0) {
                      console.log(payload);
                  } else if (i == 1) {
                      console.log("Received miner's guess: " + payload);
                      let mn = sha256( payload + sha256(2) );
                      console.log("Sending merkle number: " + mn);
                      client.send(src, mn);
                  } else {
                      client.send(src, me + 'got it ' + i);
                  }
                  i++;
              });
});





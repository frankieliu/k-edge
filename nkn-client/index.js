
const nkn = require('nkn-client');
// const client = nkn();
const client = nkn({
    identifier: 'id1',
    privateKey: '1'
});
console.log(client.key.privateKey, client.key.publicKey);
console.log(client.addr);

client.on('connect', () => {
    console.log('Connection opened.');
});


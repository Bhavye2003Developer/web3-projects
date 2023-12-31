const { secp256k1 } = require("ethereum-cryptography/secp256k1");
const { toHex } = require("ethereum-cryptography/utils.js");

// const privateKey = toHex(secp256k1.utils.randomPrivateKey());
// const publicKey = toHex(secp256k1.getPublicKey(privateKey));

// console.log("Private key:", privateKey);
// console.log("Public key:", publicKey);

function getPublicKey(privateKey) {
    return toHex(secp256k1.getPublicKey(privateKey));
}

module.exports = { getPublicKey };
const express = require("express");
const app = express();
const cors = require("cors");
const port = 3042;
const generate = require("./scripts/generate");

app.use(cors());
app.use(express.json());

const balances = {
  // private key : amount
  "1e73487883fe1c3139732385c201ad921ba018369bf13ae799a5fec25455dc90": 100,
  "2b5697baef4ac25e87cc79f397988db7f02cab9b88e562f682091f78815af5c8": 50,
  "d63546bd8d5e46ea4620e27568b93155d4a3c7d45913fe65be04a6e54b6f4809": 75,
};

app.get("/balance/:address", (req, res) => {
  const { address } = req.params;
  const balance = balances[address] || 0;
  res.send({ balance });
});

app.post("/send", (req, res) => {

  const { sender, recipient, amount } = req.body;

  const publicKey = generate.getPublicKey(sender);
  console.log("publicKey", publicKey);

  // console.log("sender", sender);

  setInitialBalance(sender);
  setInitialBalance(recipient);

  if (balances[sender] < amount) {
    res.status(400).send({ message: "Not enough funds!" });
  } else {
    balances[sender] -= amount;
    balances[recipient] += amount;
    res.send({ balance: balances[sender] });
  }
});

app.listen(port, () => {
  console.log(`Listening on port ${port}!`);
});

function setInitialBalance(address) {
  if (!balances[address]) {
    balances[address] = 0;
  }
}

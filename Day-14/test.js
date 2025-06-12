const products = [
  { name: "Pen", price: 10 },
  { name: "Notebook", price: 50 }
];

const discounted = products.map(p => ({
  name: p.name,
  price: p.price * 0.9
}));

console.log(discounted);

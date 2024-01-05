// Утилиты

function toNum(str) {
  const num = Number(str.replace(/ /g, ""));
  return num;
}


// Корзина

const cardAddArr = Array.from(document.querySelectorAll(".card__add"));
const cartNum = document.querySelector("#cart_num");
const cart = document.querySelector("#cart");

class Cart {
  products;
  constructor() {
    this.products = [];
  }
  get count() {
    return this.products.length;
  }
  addProduct(product) {
    this.products.push(product);
  }
  removeProduct(index) {
    this.products.splice(index, 1);
  }
  
  
}

class Product {
  prod_name;
  prod_quantity;
  constructor(card) {
    this.prod_name = card.querySelector(".add__name").innerText;
    this.prod_quantity = 1;
  }
}

const myCart = new Cart();

if (localStorage.getItem("cart") == null) {
  localStorage.setItem("cart", JSON.stringify(myCart));
}

const savedCart = JSON.parse(localStorage.getItem("cart"));
myCart.products = savedCart.products;
cartNum.textContent = myCart.count;

myCart.products = cardAddArr.forEach((cardAdd) => {
  cardAdd.addEventListener("click", (e) => {
    e.preventDefault();
    const card = e.target.closest(".add_prod");
    const product = new Product(card);
    const savedCart = JSON.parse(localStorage.getItem("cart"));
    
    myCart.products = savedCart ? savedCart.products : [];
    const result = myCart.products.findIndex((cartItem) => {
      return cartItem.prod_name === product.prod_name

    });
    if(result !== -1){
      myCart.products[result].prod_quantity += 1;
    } else { // если товара в корзине еще нет, то добавляем в объект
      myCart.addProduct(product);

    }

    localStorage.setItem("cart", JSON.stringify(myCart));
    cartNum.textContent = myCart.count;
  });
});

// Попап

const popup = document.querySelector(".popup");
const popupClose = document.querySelector("#popup_close");
const popupClear = document.querySelector("#popup_clear");
const body = document.body;
const popupContainer = document.querySelector("#popup_container");
const popupProductList = document.querySelector("#popup_product_list");
const popupCost = document.querySelector("#popup_cost");


function popupContainerFill() {
  popupProductList.innerHTML = null;
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  myCart.products = savedCart ? savedCart.products : [];

  const productsHTML = myCart.products.map((product) => {
    const productItem = document.createElement("div");
    productItem.classList.add("popup__product");

    const productWrap1 = document.createElement("div");
    productWrap1.classList.add("popup__product-wrap");
    const productWrap2 = document.createElement("div");
    productWrap2.classList.add("popup__product-wrap");

    const productTitle = document.createElement("p");
    productTitle.classList.add("popup__product-title");
    productTitle.innerHTML = product.prod_name;

    const productQuantity = document.createElement("div");
    productQuantity.classList.add("popup__product-quantity");
    productQuantity.innerHTML = product.prod_quantity;

    const productDelete = document.createElement("button");
    productDelete.classList.add("popup__product-delete");
    productDelete.innerHTML = "&#10006;";

    

    productDelete.addEventListener("click", () => {
      myCart.removeProduct(product);
      localStorage.setItem("cart", JSON.stringify(myCart));
      popupContainerFill();
      cartNum.textContent = myCart.count;
    });

    

    productWrap1.appendChild(productTitle);
    productWrap2.appendChild(productQuantity);
    productWrap2.appendChild(productDelete);
    productItem.appendChild(productWrap1);
    productItem.appendChild(productWrap2);


    return productItem;
  });

  productsHTML.forEach((productHTML) => {
    popupProductList.appendChild(productHTML);
  });

  
  popupCost.value = myCart.count;
  

};

// function popupMessage () {
//   const savedCart = JSON.parse(localStorage.getItem("cart"));
//   myCart.products = savedCart ? savedCart.products : [];

//   // Создаем HTML-таблицу и вставляем в поле inputMessage
//   const table = document.createElement('table');
//   table.classList.add('cart-table');

//   // Создаем заголовок таблицы
//   const thead = document.createElement('thead');
//   const headerRow = document.createElement('tr');

//   const headerName = document.createElement('th');
//   headerName.textContent = 'Наименование';

//   const headerQuantity = document.createElement('th');
//   headerQuantity.textContent = 'Количество';

//   headerRow.appendChild(headerName);
//   headerRow.appendChild(headerQuantity);
//   thead.appendChild(headerRow);
//   table.appendChild(thead);

//   // Создаем строки таблицы с данными из корзины
//   const tbody = document.createElement('tbody');
//   myCart.products.forEach(product => {
//     const row = document.createElement('tr');

//     const cellName = document.createElement('td');
//     cellName.textContent = product.prod_name;

//     const cellQuantity = document.createElement('td');
//     cellQuantity.textContent = product.prod_quantity;

//     row.appendChild(cellName);
//     row.appendChild(cellQuantity);

//     tbody.appendChild(row);
//   });

//   table.appendChild(tbody);
//   console.log(table);
//   const tableHTML = table.outerHTML.replace(/></g, '>\n<')
//   // Очищаем поле inputMessage и добавляем таблицу
//   const inputMessage = document.getElementById('inputMessage');
//   inputMessage.innerHTML = tableHTML;

// };

function popupMessage () {
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  myCart.products = savedCart ? savedCart.products : [];

  var messageData = `Наименование \t\t\t\t\t\t\t Количество\n`;
  messageData += myCart.products.map(product => `${product.prod_name}\t\t\t\t\t\t ${product.prod_quantity}\n`).join('');
  const inputMessage = document.getElementById('inputMessage');
  inputMessage.value = messageData;
};

popupClear.addEventListener("click", () => {
  myCart.products = []
  localStorage.removeItem("cart")
  cartNum.textContent = myCart.count;;
  popupCost.value = 0;
  popupContainerFill();

});

// Добавляем кнопку и событие для вставки данных в поле inputMessage
const insertDataButton = document.getElementById('insertDataButton');
insertDataButton.addEventListener('click', (e) => {
  e.preventDefault();
  popupMessage();
});

popupClose.addEventListener("click", (e) => {
  e.preventDefault();
  popup.classList.remove("popup--open");
  body.classList.remove("lock");
  cartNum.textContent = myCart.count;
});

cart.addEventListener("click", (e) => {
  e.preventDefault();
  popup.classList.add("popup--open");
  body.classList.add("lock");
  popupContainerFill();
});



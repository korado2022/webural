// При загрузке страницы проверяем localStorage на наличие данных о корзине
        let cart = JSON.parse(localStorage.getItem('cart')) || {};
        let body = document.body;
// Функция добавления товара в корзину
        function addToCart(productId) {
            cart[productId] = (cart[productId] || 0) + 1;
            localStorage.setItem('cart', JSON.stringify(cart));
        }

        // Функция обновления числа товаров в корзине
        function updateCartNum() {
            let cartNum = 0;
            for (let key in cart) {
                cartNum += cart[key];
            }
            document.getElementById('cart_num').innerText = cartNum;
        }

function removeFromCart (productName) {
    delete cart[productName];
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartNum();
}

function insertMessage () {
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  let cart = savedCart;

  var messageData = `Наименование \t\t\t\t\t\t\t Количество\n`;
  // messageData += cart.map(key => `${key}\t\t\t\t\t\t ${cart[key]}\n`).join('');
  for (key in cart) {
    messageData += `${key}\t\t\t\t\t\t ${cart[key]}\n`;
  }
  const inputMessage = document.getElementById('inputMessage');
  inputMessage.value = messageData;
};

// Добавляем кнопку и событие для вставки данных в поле inputMessage
const insertDataButton = document.getElementById('insertDataButton');
insertDataButton.addEventListener('click', (e) => {
  e.preventDefault();
  insertMessage();
});

// Функция показа корзины
        function showCart() {
            body.classList.add("lock");
            let cartContent = document.getElementById('cartContent');
            let cartTableBody = document.getElementById('cartTableBody');
            cartTableBody.innerHTML = '';

            for (let key in cart) {
                let row = document.createElement('tr');

                let nameCell = document.createElement('td');
                nameCell.innerText = key;
                row.appendChild(nameCell);

                let quantityCell = document.createElement('td');
                // Добавляем поле ввода
                let quantityInput = document.createElement('input');
                quantityInput.type = 'number';
                quantityInput.className = 'quant_input'
                quantityInput.value = cart[key];
                quantityInput.min = 1;
                quantityInput.addEventListener('input', function () {
                    updateCartItemQuantity(key, parseInt(quantityInput.value));
                    showCart();
                });
                quantityCell.appendChild(quantityInput);

                // // Добавляем кнопку "+"
                // let incrementButton = document.createElement('button');
                // incrementButton.innerText = '+';
                // incrementButton.className = 'increment-btn';
                // incrementButton.onclick = function () {
                //     updateCartItemQuantity(key, cart[key] + 1);
                //     showCart();
                // };
                // quantityCell.appendChild(incrementButton);

                // // Добавляем кнопку "-"
                // let decrementButton = document.createElement('button');
                // decrementButton.innerText = '-';
                // decrementButton.className = 'decrement-btn';
                // decrementButton.onclick = function () {
                //     if (cart[key] > 1) {
                //         updateCartItemQuantity(key, cart[key] - 1);
                //         showCart();
                //     }
                // };
                // quantityCell.appendChild(decrementButton);
                row.appendChild(quantityCell);

                let deleteCell = document.createElement('td');
                let deleteButton = document.createElement("button");
                deleteButton.innerHTML = "&#10006;";
                deleteButton.className = "remove-btn";
                deleteButton.onclick = function () {
                    removeFromCart(key);
                    showCart();
                }
                deleteCell.appendChild(deleteButton);
                row.appendChild(deleteCell);

                cartTableBody.appendChild(row);
            }

            cartContent.style.display = 'block';
        }

function updateCartItemQuantity(productName, newQuantity) {
    cart[productName] = newQuantity;
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartNum();
}
// Функция скрытия корзины
        function hideCart() {
            let cartContent = document.getElementById('cartContent');
            cartContent.style.display = 'none';
            body.classList.remove("lock");
        }

function clearCart() {
	cart = {};
	// localStorage.setItem('cart', JSON.stringify(cart));
    localStorage.removeItem("cart")
    updateCartNum();
    showCart();
}

document.addEventListener('DOMContentLoaded', function () {
        
       

        // Находим все кнопки "В корзину"
        let addToCartButtons = document.querySelectorAll('.card__add');

        // Добавляем обработчик события на каждую кнопку
        addToCartButtons.forEach(function (button) {
            button.addEventListener('click', function () {
                addToCart(button.getAttribute('data-name'));
                updateCartNum();
            });
        });
         updateCartNum();
    });

document.addEventListener("DOMContentLoaded", function () {
        const menuList = document.getElementById("menu-list");
        const burger = document.querySelector('.burger');

        burger.addEventListener("click", function () {
            menuList.classList.toggle("show-menu");
            burger.classList.toggle('active');
        });
  });
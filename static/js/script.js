// размер картинок (все картинки — равные друг другу квадраты)
        const PIC_SIZE = 436;
        // размер области просмотра карусели картинок
        const VIEWPORT_SIZE = PIC_SIZE * 3;

        // настройка ширины карусели и области просмотра карусели
        let viewport = document.getElementById("viewport");

        // количество картинок в шаге карусели
        const STEP = 1;

        function move(direction, num) {
            const NUM_PIC = document.querySelectorAll(".car_li").length;
            let ul = document.querySelector(num);
            let x = ul.style.left;        // получим координату списка
            if (x == "") { x = 0; }
            else { x = x.slice(0, -2); }  // удалим символы "px"

            if (direction) {
                x = +x + PIC_SIZE * STEP; // двигаем список вправо (кнопка «влево»)
                if (x > 0) x = 0;         // ограничитель справа
            } else {
                x = +x - PIC_SIZE * STEP; // двигаем список влево (кнопка «вправо»)
                let min = -(NUM_PIC * PIC_SIZE - VIEWPORT_SIZE);
                if (x < min) x = min;     // ограничитель слева
            }

            ul.style.left = x + "px";     // запишем вычисленную координату
        };

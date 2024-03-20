var recent_tile;
var balance = 0;
var current_answers;

function create_grid(width, height) {
    const plot = document.getElementById("plot-container");
    for (let i = 0; i < width * height; i++) {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        //add dirt img
        const dirtImg = document.createElement("img");
        dirtImg.src = "../static/index/images/dirt.png";
        tile.appendChild(dirtImg);
        // make clickable:
        dirtImg.setAttribute("data-index", i); // store index.
        tile.addEventListener("click", tileClickHandler); // add click event.
        plot.appendChild(tile);
    }
}

function populate_t() {
    var garden_string = document.getElementById("garden-string").innerHTML;
    const tiles = document.getElementById("plot-container").childNodes;

    for (let i = 0; i < tiles.length; i++) {
        var garden_tile = garden_string.charAt(i);

        switch (garden_tile) {
            case "F":
                tiles[i].childNodes[0].src = "../static/index/images/flowers.png";
                break;
            case "G":
                tiles[i].childNodes[0].src = "../static/index/images/grass.png";
                break;
            case "P":
                tiles[i].childNodes[0].src = "../static/index/images/palm.png";
                break;
            case "p":
                tiles[i].childNodes[0].src = "../static/index/images/pink-flower.png";
                break;
            case "S":
                tiles[i].childNodes[0].src = "../static/index/images/snow-bush.png";
                break;
            case "T":
                tiles[i].childNodes[0].src = "../static/index/images/trees.png";
                break;
            default:
                tiles[i].childNodes[0].src = "../static/index/images/dirt.png";
        }
    }
}

function get_garden() {
    const plot = document.getElementById("plot-container");
    const tiles = plot.childNodes;
    let garden = "";
    for (let i = 0; i < tiles.length; i++) {
        var image = tiles[i].childNodes[0].src;
        // split down to tile type, i.e.: dirt, flowers, etc.
        var parts = image.split('/');
        var file = parts[parts.length - 1];
        var tile_type = file.split('.')[0];

        switch(tile_type) {
            case "flowers":
                garden += "F";
                break;
            case "grass":
                garden += "G";
                break;
            case "palm":
                garden += "P";
                break;
            case "pink-flower":
                garden += "p";
                break;
            case "trees":
                garden += "T";
                break;
            case "snow-bush":
                garden += "S";
                break;
            default:
                garden += "D";
        }
    }
    return garden;
}

function store_garden() {
    $.post("store_garden/",
    {
      garden: get_garden(),
      csrfmiddlewaretoken: getCookie("csrftoken")
    },
    function(){
      console.log("Successfully stored garden");
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document
        .getElementById("profileButton")
        .addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent event propagation
            toggleVisibility("profileInfo");
        });

    document
        .getElementById("shopButton")
        .addEventListener("click", function (event) {
            event.stopPropagation(); // Prevent event propagation
            toggleVisibility("shopInfo");
        });

    // Add event listener to hide profile/shop div when clicking outside
    document.addEventListener("click", function (event) {
        const profileDiv = document.getElementById("profileInfo");
        const shopDiv = document.getElementById("shopInfo");
        if (!profileDiv.contains(event.target)) {
            profileDiv.style.display = "none";
        }
        if (!shopDiv.contains(event.target)) {
            shopDiv.style.display = "none";
        }
    });

    document.getElementById("flower").addEventListener("click", purchase);
    document.getElementById("tree").addEventListener("click", purchase);
    document.getElementById("grass").addEventListener("click", purchase);
    document.getElementById("palm").addEventListener("click", purchase);
    document.getElementById("pink").addEventListener("click", purchase);
    document.getElementById("snow").addEventListener("click", purchase);
});

function toggleVisibility(divId) {
    var div = document.getElementById(divId);
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function tileClickHandler(event) {
    // get the index of the clicked tile.
    const index = event.target.getAttribute("data-index");
    event.stopPropagation();
    toggleVisibility("shopInfo");
    recent_tile = index;
    console.log("Tile index", index, " clicked.");
}

function load_balance() {
    var coins_string = document.getElementById("coins").innerHTML;
    balance = parseInt(coins_string.match(/\d+/)[0], 10);
    console.log("Current Balance: " + balance);
}

function purchase(event) {
    event.stopPropagation();
    /*
    Costs: 
    Flower = 20
    Tree = 40
    Grass = 10
    */
   load_balance();
    var tree = document.createElement("img");
    tree.src = "../static/index/images/trees.png";
    var flower = document.createElement("img");
    flower.src = "../static/index/images/flowers.png";
    var grass = document.createElement("img");
    grass.src = "../static/index/images/grass.png";
    var palm = document.createElement("img");
    palm.src = "../static/index/images/palm.png";
    var snow = document.createElement("img");
    snow.src = "../static/index/images/snow-bush.png";
    var pink = document.createElement("img");
    pink.src = "../static/index/images/pink-flower.png";

    const tile = get_tile(recent_tile);
    if (event.target.id === "flower" && balance >= 20) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(flower);
        update_balance(20, "subtract");
    } else if (event.target.id === "tree" && balance >= 40) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(tree);
        update_balance(40, "subtract");
    } else if (event.target.id === "grass" && balance >= 10) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(grass);
        update_balance(10, "subtract");
    } else if (event.target.id === "palm" && balance >= 50) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(palm);
        update_balance(50, "subtract");
    } else if (event.target.id === "snow" && balance >= 25) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(snow);
        update_balance(25, "subtract");
    } else if (event.target.id === "pink" && balance >= 20) {
        toggleVisibility("shopInfo");
        tile.innerHTML = "";
        tile.appendChild(pink);
        update_balance(20, "subtract");
    }
    post_balance(balance);
    store_garden();
    toggleVisibility("shopInfo");
}

function get_tile(index) {
    const plot_cont = document.getElementById("plot-container");
    const tiles = plot_cont.childNodes;

    if (index >= 0 && index < tiles.length) {
        return tiles[index];
    } else {
        console.error("Invalid tile index:", index);
        return null;
    }
}

// update balance for when an item is bought
function update_balance(cost, operation) {
    if (operation === "add") {
        balance += cost;
    } else {
        balance -= cost;
    }
    post_balance(balance);
    var balance_string = "Coins: " + balance;
    document.getElementById("coins").innerHTML = balance_string;
    document.getElementById("coinsCounter").innerHTML = balance_string;
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
}

function post_balance(balance) {
    $.post("update_coins/",
    {
      balance: balance,
      csrfmiddlewaretoken: getCookie("csrftoken")
    },
    function(data,status){
      console.log("Successfully updated balance");
    });
}

let bottomBarLocked = false;
document.addEventListener("DOMContentLoaded", function () {
    var bottomBarButton = document.getElementById("bottomBarButton");
    var bottomBarContent = document.getElementById("bottomBarContent");
    var bottomBar = document.getElementById("bottomBar");

    bottomBarButton.addEventListener("click", function () {
        if (!bottomBarLocked) {
            if (bottomBarContent.style.display === "none") {
                bottomBarContent.style.display = "block";
                bottomBarButton.innerHTML =
                    '<img src="../static/index/images/down.png" alt="">';

                bottomBar.classList.add("open");
            } else {
                bottomBarContent.style.display = "none";
                bottomBarButton.innerHTML =
                    '<img src="../static/index/images/up.png" alt="">';
                bottomBar.classList.remove("open");
            }
        }
    });
});

function format_challenges() {
    question_div = document.getElementById("question");
    answers_div = document.getElementById("answers-gen");
    answers_list = answers_div.innerHTML;
    answers_list = answers_list.replace(/'/g, '"');
    const answers = JSON.parse(answers_list);
    current_answers = answers;
    // another list with the answers shuffled.
    const shuffled = shuffle_list([...answers]);

    answers_div.innerHTML = "";
    
    form = document.getElementById("fact-match");
    for (let i = 0; i < shuffled.length; i++) {
        var div = document.createElement("div");
        var label = document.createElement("label");
        label.textContent = shuffled[i];
        label.id = "label-select" + (i+1);
        var select = document.createElement("select");
        select.name = "position";
        select.id = "select" + (i+1);

        for (let j = 1; j <= answers.length; j++) {
            var option = document.createElement("option");
            option.value = j;
            option.textContent = j;
            select.appendChild(option);
        }
        div.appendChild(label);
        div.appendChild(select);
        form.appendChild(div);
    }
    var submit = document.createElement("input");
    submit.type = "submit"
    submit.value = "Submit"
    form.appendChild(submit);
    toggleVisibility("answer-input");
}

function shuffle_list(list) {
    for (let i = list.length - 1; i>0; i--) {
        const j = Math.floor(Math.random() * (i+1));
        [list[i], list[j]] = [list[j], list[i]];
    }
    return list;
}

function check_answers() {
    var reward = 0;
    for (let i = 0; i < current_answers.length; i++) {
        var select_val = document.getElementById("select" + (i+1)).value;
        var select_label = document.getElementById("label-select" + (i+1)).innerHTML;

        if (select_label == current_answers[parseInt(select_val)-1]) {
            reward += 10;
        }
    }
    
    if (reward/10 == current_answers.length) {
        alert("Well Done! All your answers were correct. Reward: " + reward + " credits added to your balance.");
    }
    else if (reward == 0) {
        alert("No answers were correct. Try again tomorrow!")
    }
    else {
        alert("Congrats " + (reward/10) + " of your answers were correct. You won " + reward + " credits. See you tomorrow!");
    }

    // set cookie as timer till next day
    var expiration = new Date();
    expiration.setDate(expiration.getDate()+1);
    document.cookie="fmComplete=True; expires=" + expiration.toUTCString() + "; path=/";

    update_balance(reward, "add");
}

function toggleForms() {
    var loginForm = document.getElementById("login_form");
    var registerForm = document.getElementById("register_form");

    if (loginForm.style.display === "none") {
        loginForm.style.display = "block";
        registerForm.style.display = "none";
    } else {
        loginForm.style.display = "none";
        registerForm.style.display = "block";
    }
}
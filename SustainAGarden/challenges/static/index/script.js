var recent_tile;
var balance = 0;

function create_grid(width, height) {
    const plot = document.getElementById("plot-container");
    for (let i = 0; i < width * height; i++) {
        const tile = document.createElement("div");
        tile.classList.add("tile");
        // make clickable:
        tile.setAttribute("data-index", i); // store index.
        tile.addEventListener("click", tileClickHandler); // add click event.
        plot.appendChild(tile);
    }
}

function populate_t(tile_string) {
    const plot = document.getElementById("plot-container");
    const tiles = plot.childNodes;
    for (let i = 0; i < tile_string.length; i++) {
        if (tile_string[i] != "0") {
            tiles[i].textContent = tile_string[i];
        }
    }
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
    var coins_string = document.getElementById("coins").textContent;
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

    const tile = get_tile(recent_tile);
    if (event.target.id === "flower" && balance >= 20) {
        tile.textContent = "F";
        tile.style.backgroundColor = "pink";
        update_balance(20, "subtract");
        toggleVisibility("shopInfo");
    } else if (event.target.id === "tree" && balance >= 40) {
        tile.textContent = "T";
        tile.style.backgroundColor = "green";
        update_balance(40, "subtract");
        toggleVisibility("shopInfo");
    } else if (event.target.id === "grass" && balance >= 10) {
        tile.textContent = "G";
        tile.style.backgroundColor = "lightgreen";
        update_balance(10, "subtract");
        toggleVisibility("shopInfo");
    }
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
    var balance_string = "Coins: " + balance;
    document.getElementById("coins").textContent = balance_string;
    document.getElementById("coinsCounter").textContent = balance_string;
}

document.addEventListener("DOMContentLoaded", function () {
    var bottomBarButton = document.getElementById("bottomBarButton");
    var bottomBarContent = document.getElementById("bottomBarContent");
    var bottomBar = document.getElementById("bottomBar");

    bottomBarButton.addEventListener("click", function () {
        if (bottomBarContent.style.display === "none") {
            bottomBarContent.style.display = "block";
            bottomBarButton.innerHTML =
                '<img src="../static/index/down.png" alt="">';

            bottomBar.classList.add("open");
        } else {
            bottomBarContent.style.display = "none";
            bottomBarButton.innerHTML =
                '<img src="../static/index/up.png" alt="">';
            bottomBar.classList.remove("open");
        }
    });
});

function checkAnswers() {
    let rewards = 0;

    // Check answers for challenge 1
    let q1Answer = document.querySelector('input[name="ans-q1"]:checked');
    if (q1Answer && q1Answer.value === "7") {
        rewards += parseInt(
            document.querySelector("#challenge3 .reward").textContent
        );
    }

    // Check answers for challenge 2
    let q2Answer = document.querySelector('input[name="ans-q2"]:checked');
    if (q2Answer && q2Answer.value === "103000") {
        rewards += parseInt(
            document.querySelector("#challenge3 .reward").textContent
        );
    }

    // Check answers for challenge 3
    let blanks = document.querySelectorAll('#challenge3 input[name^="ans-b"]');
    let blankAnswers = [];
    blanks.forEach((blank) => {
        if (blank.checked) {
            blankAnswers.push(blank.value);
        }
    });
    if (
        blankAnswers.length === 5 &&
        blankAnswers[0] === "planglow" &&
        blankAnswers[1] === "polystyrene" &&
        blankAnswers[2] === "plant-based" &&
        blankAnswers[3] === "wood" &&
        blankAnswers[4] === "plantations"
    ) {
        rewards += parseInt(
            document.querySelector("#challenge3 .reward").textContent
        );
    }

    document.getElementById("bottomBar").style.display = "none";
    alert(rewards + " Coins won.");
    update_balance(rewards, "add");
}

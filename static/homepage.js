const wrapper = document.getElementById("tiles");

let columns = 0,
    rows = 0,
    toggled = false;

const toggle = () => {
  toggled = !toggled;
  
  document.body.classList.toggle("toggled");
}


const createTile = index => {
  const tile = document.createElement("div");
  
  tile.classList.add("tile");
  
  tile.style.opacity = toggled ? 0 : 1;
  
  
  return tile;
}

const createTiles = quantity => {
  Array.from(Array(quantity)).map((tile, index) => {
    wrapper.appendChild(createTile(index));
  });
}

const createGrid = () => {
  wrapper.innerHTML = "";
  
  const size = document.body.clientWidth > 800 ? 100 : 50;
  
  columns = Math.floor(document.body.clientWidth / size);
  rows = Math.floor(document.body.clientHeight / size);
  
  wrapper.style.setProperty("--columns", columns);
  wrapper.style.setProperty("--rows", rows);
  
  createTiles(columns * rows);
}

createGrid();

window.onresize = () => createGrid();

// Get references to the input element and the table body
var input = document.getElementById('username');
var table = document.getElementById('leaderboard');

// Add an event listener to the input element
input.addEventListener('keyup', function() {
    // Get the current value of the input
    var filter = input.value.toUpperCase();

    // Get all the rows in the table
    var rows = table.querySelectorAll('tr[data-username]');

    // Loop through each row
    for (var i = 0; i < rows.length; i++) {
        // Get the username for this row
        var username = rows[i].getAttribute('data-username');

        // If the username includes the filter, show the row, otherwise hide it
        if (username.toUpperCase().includes(filter)) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
});

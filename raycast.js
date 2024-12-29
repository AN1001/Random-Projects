const canvas = document.createElement("canvas")
const ctx = canvas.getContext("2d")
document.body.appendChild(canvas)

function drawGrid(grid, boxWidth, boxHeight) {
  canvas.width = grid[0].length * boxWidth
  canvas.height = grid.length * boxHeight

  grid.forEach((row, y) => {
    row.forEach((cell, x) => {
      ctx.fillStyle = cell === 1 ? "black" : "white"
      ctx.fillRect(x * boxWidth, y * boxHeight, boxWidth, boxHeight)
      ctx.strokeRect(x * boxWidth, y * boxHeight, boxWidth, boxHeight)
    })
  })
}

function drawLine(x1, y1, x2, y2) {
  x1 = x1 * boxWidth
  x2 = x2 * boxWidth
  y1 = y1 * boxHeight
  y2 = y2 * boxHeight
  ctx.beginPath()
  ctx.moveTo(x1, y1)
  ctx.lineTo(x2, y2)
  ctx.strokeStyle = "red"
  ctx.lineWidth = 2
  ctx.stroke()
}

function cast_ray(pos_x, pos_y, ray_dir_x, ray_dir_y, worldMap) {
        //which box of the map we're in
      let mapX = parseInt(pos_x);
      let mapY = parseInt(pos_y);

      //length of ray from current position to next x or y-side
      let sideDistX;
      let sideDistY;

       //length of ray from one x or y-side to next x or y-side
      let deltaDistX = (ray_dir_x === 0) ? 1e30 : Math.abs(1 / ray_dir_x);
      let deltaDistY = (ray_dir_y === 0) ? 1e30 : Math.abs(1 / ray_dir_y);
      let perpWallDist;

      //what direction to step in x or y-direction (either +1 or -1)
      let stepX;
      let stepY;

      let hit = 0; //was there a wall hit?
      let side; //was a NS or a EW wall hit?

      if (ray_dir_x < 0)
      {
        stepX = -1;
        sideDistX = (posX - mapX) * deltaDistX;
      }
      else
      {
        stepX = 1;
        sideDistX = (mapX + 1.0 - pos_x) * deltaDistX;
      }
      if (ray_dir_y < 0)
      {
        stepY = -1;
        sideDistY = (pos_y - mapY) * deltaDistY;
      }
      else
      {
        stepY = 1;
        sideDistY = (mapY + 1.0 - pos_y) * deltaDistY;
      }
      //perform DDA
      while (hit === 0)
      {
        //jump to next map square, either in x-direction, or in y-direction
        if (sideDistX < sideDistY)
        {
          sideDistX += deltaDistX;
          mapX += stepX;
          side = 0;
        }
        else
        {
          sideDistY += deltaDistY;
          mapY += stepY;
          side = 1;
        }
        //Check if ray has hit a wall
        if (worldMap[mapX][mapY] > 0) hit = 1;
      } 

			console.log(mapX, mapY)
      return [sideDistX+deltaDistX, sideDistY+deltaDistY];
}

function cast_rays() {
  var posX = 22
  var posY = 12 //x and y start position
  var dirX = -1
  var dirY = 0 //initial direction vector
  var planeX = 0
  var planeY = 0.66 //the 2d raycaster version of camera plane

  var time = 0 //time of current frame
  var oldTime = 0 //time of previous frame
}
// Example usage:
const grid = [
  [1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1],
]

const boxWidth = 50;
const boxHeight = 50;
const px = 1.1;
const py = 1.1;
drawGrid(grid, boxWidth, boxHeight)


ray = (cast_ray(px, py, 4, 1, grid))
console.log(ray)
drawLine(px, py, ray[0]+0.1+1, ray[1]+0.1+1)

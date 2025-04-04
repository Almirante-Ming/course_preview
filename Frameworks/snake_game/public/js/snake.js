const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');

const size = 20;

let snake = [
  { x: 200, y: 200 }
];

let direction = { x: 0, y: 0 };
let snakeLength = 1;

function drawSnake() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'lime';

  for (let part of snake) {
    ctx.fillRect(part.x, part.y, size, size);
  }
}

function moveSnake() {
  const head = snake[snake.length - 1];

  const newHead = {
    x: head.x + direction.x * size,
    y: head.y + direction.y * size
  };

  if (newHead.x < 0) newHead.x = canvas.width - size;
  if (newHead.x >= canvas.width) newHead.x = 0;
  if (newHead.y < 0) newHead.y = canvas.height - size;
  if (newHead.y >= canvas.height) newHead.y = 0;

  snake.push(newHead);

  while (snake.length > snakeLength) {
    snake.shift();
  }

  drawSnake();
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowUp') {
    direction = { x: 0, y: -1 };
  } else if (e.key === 'ArrowDown') {
    direction = { x: 0, y: 1 };
  } else if (e.key === 'ArrowLeft') {
    direction = { x: -1, y: 0 };
  } else if (e.key === 'ArrowRight') {
    direction = { x: 1, y: 0 };
  } else if (e.key === ' ') {
    e.preventDefault();
    snakeLength++;
    if (direction.x === 0 && direction.y === 0) drawSnake();
  } else if (e.key === 'Backspace') {
    e.preventDefault();
    if (snakeLength > 1) {
      snakeLength--;
      if (direction.x === 0 && direction.y === 0) {
        snake.shift();
        drawSnake();
      }
    }
  }
});

setInterval(moveSnake, 150);
drawSnake();
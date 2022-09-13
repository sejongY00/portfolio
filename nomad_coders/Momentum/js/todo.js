const toDoForm = document.querySelector("#todo-form");
const toDoInput = toDoForm.querySelector("input");
const toDoList = document.querySelector("#todo-list");

const TODOS_KEY = "todos";

let toDos = [];

function deleteTodo(event) {
  const li = event.target.parentElement;
  toDos = toDos.filter((toDo) => toDo.id != li.id);
  li.remove();
  saveToDos();
}

function saveToDos() {
  localStorage.setItem("todos", JSON.stringify(toDos));
}

function paintToDo(newTodoObj) {
  const li = document.createElement("li");
  li.id = newTodoObj.id;
  const span = document.createElement("span");
  const button = document.createElement("button");
  button.classList.add(
    "font-bold",
    "rounded",
    "ml-3",
    "text-lg",
    "text-white",
    "hover:opacity-75",
    "bg-transparent",
    "border-2",
    "px-2"
  );
  button.innerHTML = "×";
  button.addEventListener("click", deleteTodo);
  toDoList.appendChild(li);
  li.appendChild(span);
  li.appendChild(button);
  span.innerHTML = newTodoObj.text;
}

function handleToDoSubmit(event) {
  event.preventDefault();
  const newTodo = toDoInput.value;
  toDoInput.value = "";
  const newTodoObj = { id: Date.now(), text: newTodo };
  toDos.push(newTodoObj);
  paintToDo(newTodoObj);
  saveToDos();
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if (savedToDos !== null) {
  const parsedToDos = JSON.parse(savedToDos);
  toDos = parsedToDos;
  parsedToDos.forEach(paintToDo);
}

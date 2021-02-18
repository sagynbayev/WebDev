const todoInput = document.querySelector(".TextInput");
const todoButtonSubmit = document.querySelector(".buttonAdd");
const todoList = document.querySelector(".ListofCells");


todoButtonSubmit.addEventListener('click', addCells);
todoList.addEventListener('click', deleteCheck)

function addCells(){
    // alert("hello");
    const todoDiv = document.createElement("div");
    todoDiv.classList.add("todo");
    const newTodo = document.createElement('li');
    let liText = todoInput.value;
    newTodo.innerHTML = liText;
    newTodo.classList.add('todo-item')
    todoDiv.appendChild(newTodo);

    const completedButton = document.createElement('input');
    // completedButton.innerText = 'Completed';
    completedButton.type = "checkbox";
    completedButton.classList.add("buttonComplete");
    todoDiv.appendChild(completedButton);

    const trashButton = document.createElement('button');
    trashButton.innerText = 'trash';
    trashButton.classList.add("buttonTrash");
    todoDiv.appendChild(trashButton);

    if(newTodo.innerHTML != ""){
        todoList.appendChild(todoDiv);
    }
    todoInput.value = ""
}


function deleteCheck(e){
    const item = e.target;

    if (item.classList[0] === "buttonTrash"){
        const todo = item.parentElement;
        todo.remove();
    }

    if(item.classList[0] === "buttonComplete"){
        const todo = item.parentElement;
        // todo.classList.toggle("completed");
        todo.classList.toggle("completed")
    }
}
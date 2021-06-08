function test(){
    document.getElementById("span").textContent = "Aguarde..."
    eel.test()
}

eel.expose(write_result)
function write_result(result, id){
    console.log(result)
    document.getElementById(id).textContent = result;
}

eel.expose(all_done)
function all_done(){
    document.getElementById("span").textContent = "Concluido" 
}
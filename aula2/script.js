function validarForm(){
    conteudo = document.getElementById("txtNumero").value;
    if(isNaN(conteudo) || conteudo < 1 || conteudo > 10){
        document.getElementById("info").innerHTML="Valor não permitido"
        return false;
    }else{
        return true
    }
}

function calcular(){
    n1=document.getElementById("num").value
    n2=document.getElementById("num2").value
    resp=""
    if (n1==""){
        resp+="O primeiro campo está vazio<br>"
    }else{
        if(isNaN(n1)){
            resp+="O valor do primeiro campo precisa ser um número<br> "
        }
    }
    if (n2==""){
        resp+="O segundo campo está vazio"
    }else{
        if(isNaN(n2)){
            resp+="O valor do segundo campo precisa ser um número"
        }
    }
    if (resp==""){
        n1=parseFloat(n1)
        n2=parseFloat(n2)
        document.getElementById("result").innerHTML=n1+n2
    }else{
        document.getElementById("result").innerHTML=resp
    }
}
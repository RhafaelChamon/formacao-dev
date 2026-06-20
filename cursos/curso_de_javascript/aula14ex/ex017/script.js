document.querySelector('#ger_tab').addEventListener('click', gerar_tabua)

function gerar_tabua() {
    var n = document.querySelector('#num').value
    var tabuada = document.querySelector('#resu div#tab select')
    
    if (n.length == 0) {
        alert('Por favor, insira um número.')
    } else {
        var n = Number(n)

        tabuada.innerHTML = null
        for (var i = 1 ; i <= 10 ; i++) {
            var op = document.createElement('option')
            op.value = `tab${i}`
            op.innerHTML = `${i} x ${n} = ${i * n}`
            tabuada.appendChild(op)
        }
        document.querySelector('#resu').style.display = 'block'
    }
}
document.querySelector('#bot_cont').addEventListener('click', contar)
var resu = document.createElement('div')

function contar() {
    var ini = document.querySelector('#ini').value
    var fim = document.querySelector('#fim').value
    var pas = document.querySelector('#pas').value
    
    if (ini.length == 0 || fim.length == 0 || pas.length == 0) {
        alert('[ERRO] Insira todos os dados solicitados.')
    } else {
        var ini = Number(ini)
        var fim = Number(fim)
        var pas = Number(pas)
        
        if (pas < 0) {
                pas *= -1
        } else if (pas == 0) {
            alert('Zero não pode ser considerado um passo. Valor a ser considerado: 1')
            pas = 1
        }
        
        var contagem = ''
        var i = ini
        if (ini < fim) {
            while (i <= fim) {
                contagem += `${i} &#x1f449; `
                i += pas
            }
        } else {
            while (i >= fim) {
                contagem += `${i} &#x1f449; `
                i -= pas
            }
        } 
        contagem += '&#127937;'
    
        resu.innerHTML = `<p>Contagem:</p><p id="cont">${contagem}</p>`
        document.getElementsByTagName('main')[0].appendChild(resu)
    }
}

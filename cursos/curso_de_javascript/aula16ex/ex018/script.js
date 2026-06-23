document.querySelector('#botao_add').addEventListener('click', adicionar)
document.querySelector('#botao_end button').addEventListener('click', finalizar)
let lista_valores = []
let resu = document.querySelector('#resu')

function adicionar() {
    let num = document.querySelector('#num').value
    if (validar_num(num, lista_valores)) {
        resu.style.display = 'none'
        num = Number(num)
        lista_valores.push(num)
        
        let op = document.createElement('option')
        op.value = `num${num}`
        op.text = `Valor ${num} adicionado.`
        document.querySelector('#select_num').appendChild(op)
    } else {
        alert('Valor inválido ou já encontrado na lista!')
    }
}

function finalizar() {
    if (lista_valores.length != 0) {
        let p = new Array(5).fill(null)
        let maior_num = lista_valores[0]
        let menor_num = lista_valores[0]
        let soma = 0
        let media
        
        for (let k in p) {
            p[k] = document.createElement('p')
        }
        
        for (let k of lista_valores) {
            if (k > maior_num) {
                maior_num = k
            } else if (k < menor_num) {
                menor_num = k
            }
            
            soma += k
        }
        media = soma / lista_valores.length
        
        p[0].innerText = `Ao todo, temos ${lista_valores.length} números cadastrados`
        p[1].innerText = `O maior número informado foi ${maior_num}`
        p[2].innerText = `O menor número informado foi ${menor_num}`
        p[3].innerText = `A soma de todos os números é ${soma}`
        p[4].innerText = `A média dos números é ${media}`
        
        resu.innerHTML = null
        for (let k in p) {
            resu.appendChild(p[k])
        }
        
        resu.style.display = 'block'
    } else {
        alert('Adicione valores anter de finalizar!')
    }
}

function validar_num(n, lista) {
    n = Number(n)
    if (n >= 1 && n <= 100 && lista.indexOf(n) == -1) {
        return true
    } else {
        return false
    }
}
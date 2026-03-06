const nome = document.getElementById('nome');
const email = document.getElementById('email');
const senha = document.getElementById('senha');
const confirmaSenha = document.getElementById('confirma-senha');
const form = document.getElementById('formulario');
const telefone = document.getElementById('telefone');
const cep = document.getElementById('cep');
const dataNascimento = document.getElementById('data-nascimento');
const url = document.getElementById('url');
const valor = document.getElementById('valor');

form.addEventListener('submit', (e) => {
    // Limpa mensagens anteriores
    document.getElementById('erro-nome').textContent = '';
    document.getElementById('erro-email').textContent = '';
    document.getElementById('erro-senha').textContent = '';
    document.getElementById('erro-cpf').textContent = '';
    document.getElementById('erro-telefone').textContent = '';
    document.getElementById('erro-cep').textContent = '';
    document.getElementById('erro-data-nascimento').textContent = '';
    document.getElementById('erro-valor').textContent = '';
    document.getElementById('erro-url').textContent = '';

    e.preventDefault(); // Impede o envio do formulário e o reload da página
    let enviarform = true;
    // && é um operador de (e), que retorna um valor verdadeiro se todos os campos estiverem preenchidos.
    if (!nome.value) {
        document.getElementById('erro-nome').textContent = 'O campo nome está vazio';
        enviarform = false;
    }

    //senha    
    // Verifica se a senha tem caracteres especiais, ignora letras e números usando uma array de regex
    const especiais = senha.value.match(/[^a-zA-Z0-9]/g);
    if (!especiais) {
        document.getElementById('erro-senha').textContent = 'A senha deve conter pelo menos um caractere especial';
        enviarform = false;
    }

    if (senha.value !== confirmaSenha.value) {
        document.getElementById('erro-senha').textContent = 'As senhas não coincidem';
        enviarform = false;
    }
            // Verifica se a senha tem pelo menos um número
        const temNumero = /[0-9]/.test(senha.value);
        if (!temNumero) {
            document.getElementById('erro-senha').textContent = 'A senha deve conter pelo menos um número';
            enviarform = false;
        }

        // Verifica se a senha tem pelo menos uma letra maiúscula
        const temMaiuscula = /[A-Z]/.test(senha.value);
        if (!temMaiuscula) {
            document.getElementById('erro-senha').textContent = 'A senha deve conter pelo menos uma letra maiúscula';
            enviarform = false;
        }

    if (senha.value.length < 8) {
        document.getElementById('erro-senha').textContent = 'A senha é muito curta';
        enviarform = false;
    }
    //email

    if (!email.value.includes('@')) {
        document.getElementById('erro-email').textContent = 'O e-mail deve conter @';
        enviarform = false;
    }
    if (!email.value.includes('.com')) {
        document.getElementById('erro-email').textContent = 'O e-mail deve conter .com';
        enviarform = false;
    }

    //cpf
    const cpf = document.getElementById('cpf');
    const cpfValor = cpf.value.replace(/\D/g, ''); // Remove tudo que não é número
    function validaCPF(cpf) {
        if (cpf.length !== 11 || /^(\\d)\1{10}$/.test(cpf)) return false; //verifica se o CPF tem 11 digitos e se todos os dígitos são iguais
        let soma = 0; //inicia a soma
        for (let i = 0; i < 9; i++) soma += parseInt(cpf.charAt(i)) * (10 - i); //multiplica cada dígito pelos pesos de 10 a 2 e soma os resultados
        let resto = soma % 11;//calcula o resto da divisão da soma por 11
        let digito1 = resto < 2 ? 0 : 11 - resto;//calcula o primeiro dígito verificador
        if (parseInt(cpf.charAt(9)) !== digito1) return false;//verifica se o primeiro dígito verificador é igual ao décimo dígito do CPF
        soma = 0;
        for (let i = 0; i < 10; i++) soma += parseInt(cpf.charAt(i)) * (11 - i);
        resto = soma % 11;
        let digito2 = resto < 2 ? 0 : 11 - resto;
        if (parseInt(cpf.charAt(10)) !== digito2) return false;
        return true;
    }
    if (!validaCPF(cpfValor)) {
        document.getElementById('erro-cpf').textContent = 'CPF inválido';
        enviarform = false;
    }

    //telefone
const telValor = telefone.value.replace(/\D/g, ''); // Limpa tudo

// CORREÇÃO: Usamos \d em vez de \\d
const telefoneValido = /^\d{2}\d{8,9}$/.test(telValor);

if (!telefoneValido) {
    document.getElementById('erro-telefone').textContent = 'Telefone deve ter DDD e número (10 ou 11 dígitos)';
    enviarform = false;
} else {
    document.getElementById('erro-telefone').textContent = '';
}
//CEP
const cepValor = cep.value.replace(/\D/g, ''); // Remove tudo que não é número

// Regex 8 dígitos (CEP)
const cepValido = /^\d{8}$/.test(cepValor);

if (!cepValido) {
    document.getElementById('erro-cep').textContent = 'CEP deve ter 8 dígitos';
    enviarform = false;
}
//Data 
const dataValor = dataNascimento.value;
// Validação precisa usando Date
function validaData(data) {
    const regex = /^([1-9]|[12][0-9]|3[01])\/([1-9]|1[0-2])\/\d{4}$/;
    if (!regex.test(data)) return false;
    const [dia, mes, ano] = data.split('/').map(Number);
    const dataObj = new Date(ano, mes - 1, dia);
    return (
        dataObj.getFullYear() === ano &&
        dataObj.getMonth() === mes - 1 &&
        dataObj.getDate() === dia
    );
}
if (!validaData(dataValor)) {
    document.getElementById('erro-data-nascimento').textContent = 'Data inválida';
    enviarform = false;
}
//verifica a url, começa com https ou http
const urlValor = url.value;
// o .startsWith verifica se a string começa com o valor especifico
if (!url.value.startsWith('https://') && !url.value.startsWith('http://')) {
    document.getElementById('erro-url').textContent = 'URL deve conter https:// ou http://';
    enviarform = false;
}
//valor monetario
const valorValor = valor.value;
const valorValido = /^\d{1,3}(\.\d{3})*,\d{2}$/.test(valorValor);
if (!valorValido) {
    document.getElementById('erro-valor').textContent = 'Valor deve estar no formato R$ 1.234,56';
    enviarform = false;
}
});
function validaCartao(numeroLimpo) {
    // 1. Ajuste do tamanho: Amex tem 15, os outros 16. 
    // Aceitamos de 15 a 16 para não travar a bandeira.
    if (numeroLimpo.length < 15 || numeroLimpo.length > 16) {
        document.getElementById('bandeira').textContent = ""; 
        return false;
    }

    let bandeira = 'Bandeira desconhecida';

    // 2. Identificação das bandeiras
    if (/^4/.test(numeroLimpo)) {
        bandeira = 'Visa';
        //teste é mais simples que match ele volta ou um True ou False.
    } else if (/^5[1-5]/.test(numeroLimpo)) {
        bandeira = 'MasterCard';
    } else if (/^3[47]/.test(numeroLimpo)) {
        bandeira = 'American Express';
    } else if (/^6(?:011|5)/.test(numeroLimpo)) {
        bandeira = 'Discover';
    }

    // 3. Atualiza o texto na tela uma única vez (mais limpo!)
    document.getElementById('bandeira').textContent = `Bandeira do cartão: ${bandeira}`;

    // 4. Se a bandeira for desconhecida, talvez o cartão seja inválido
    if (bandeira === 'Bandeira desconhecida') return false;

    return true;
}

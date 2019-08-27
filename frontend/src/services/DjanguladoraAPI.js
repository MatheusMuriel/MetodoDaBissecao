import axios from 'axios';

//const urlBaseMarvel = 'https://gateway.marvel.com:443/v1/public/';
//const apiKey = 'CHAVE-PUBLICA-MARVEL-API';
const urlBaseDjanguladora = 'http://localhost:8000/';

export default {
    calculaFuncao: (header, callback) => {
        console.log('Chamou')
        const urlCalculo = urlBaseDjanguladora + 'calculo';

        axios({
            method: 'get',
            url: urlCalculo,
            responseType: 'stream'
          }).then(function (response) {
              console.log(response)
          });
    },
    calculaPost: (x5, x4, x3, x2, x1, xf, epsilon) => {
				let urlPost = urlBaseDjanguladora + 'calculo/'
				console.log('Chegou na api')
        axios({
            method: 'post',
            url: urlPost,
            data: {
              funcao: 'Fred',
              lastName: 'Flintstone',
              x5: x5,
							x4: x4,
							x3: x3,
							x2: x2,
							x1: x1,
							xf: xf,
							epsilon: epsilon,
            }
          });
    }
}
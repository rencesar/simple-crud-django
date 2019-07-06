const addressInput = document.getElementById('id_address');
const cityInput = document.getElementById('id_city');
const stateInput = document.getElementById('id_state');
const zipCodeElement = document.getElementById('id_zipcode');
const numberInput = document.getElementById('id_number');
const phoneElement = document.getElementById('id_phone');
const mapDiv = document.getElementById('id_map');

IMask(zipCodeElement, {
  mask: '00000-000'
});

IMask(phoneElement, {
  mask: '(00) 0 0000-0000'
});

const MAP_STATES = {
  'AC': 'Acre',
  'AL': 'Alagoas',
  'AP': 'Amapá',
  'AM': 'Amazonas',
  'BA': 'Bahia',
  'CE': 'Ceará',
  'DF': 'Distrito Federal',
  'ES': 'Espírito Santo',
  'GO': 'Goiás',
  'MA': 'Maranhão',
  'MT': 'Mato Grosso',
  'MS': 'Mato Grosso do Sul',
  'MG': 'Minas Gerais',
  'PA': 'Pará',
  'PB': 'Paraíba',
  'PR': 'Paraná',
  'PE': 'Pernambuco',
  'PI': 'Piauí',
  'RJ': 'Rio de Janeiro',
  'RN': 'Rio Grande do Norte',
  'RS': 'Rio Grande do Sul',
  'RO': 'Rondônia',
  'RR': 'Roraima',
  'SC': 'Santa Catarina',
  'SP': 'São Paulo',
  'SE': 'Sergipe',
  'TO': 'Tocantins'
};

let lastCepCheck = '';
let address = '';
let city = '';
let state = '';
let number = '';

async function getZipCodeEvent(event) {
  let cep = event.value.replace(/[^0-9]/, "");
  if (cep.length !== 8 || lastCepCheck === cep) {
    return false;
  }
  lastCepCheck = cep;

  let response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
  let data = await response.json();
  address = `${data.logradouro}, ${data.bairro}`;
  city = data.localidade;
  state = MAP_STATES[data.uf];
  addressInput.value = address;
  cityInput.value = city;
  stateInput.value = state;

  mapDiv.innerHTML = `
    <iframe
      width="600" height="500"
      src="https://maps.google.com/maps?q=${address} ${city} ${state}&t=&z=17&ie=UTF8&iwloc=&output=embed"
      frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
      ></iframe>
  `
}

function renderMaps(event) {
  address = addressInput.value;
  city = cityInput.value;
  state = stateInput.value;
  number = numberInput.value;

  mapDiv.innerHTML = `
    <iframe
      width="600" height="500"
      src="https://maps.google.com/maps?q=${address} ${number} ${city} ${state}&t=&z=17&ie=UTF8&iwloc=&output=embed"
      frameborder="0" scrolling="no" marginheight="0" marginwidth="0"
      ></iframe>
  `
}

let timer;
function onZipInput(event) {
    clearTimeout(timer);
    timer = setTimeout(getZipCodeEvent(this), 2000);
}

function onAddressInput(event) {
    clearTimeout(timer);
    timer = setTimeout(renderMaps(this), 5000);
}

[addressInput, cityInput, stateInput, numberInput].forEach(
  function(elem) {
    elem.addEventListener('input', onAddressInput, false);
  }
);

zipCodeElement.addEventListener('input', onZipInput, false);

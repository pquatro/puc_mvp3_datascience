/*
  --------------------------------------------------------------------------------------
  Função para obter a lista de pacientes existentes do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/pacientes';
  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => insertList(item.id,item.name, item.age, item.anae, item.crea, item.diab, 
        item.ejec,item.high,item.plate,item.ser_crea,item.ser_sodi,item.sex,item.smok,item.tim,item.death))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}
/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (id,name, age, anae, crea, diab, ejec, high, plate, ser_crea, ser_sodi, sex, smok, tim) => {
  var item = [id, name, age, anae,crea,diab,ejec,high,plate,ser_crea,ser_sodi,sex,smok,tim]
  var table = document.getElementById('myTable');
  var row = table.insertRow();
  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }
  insertButton(row.insertCell(-1))
  document.getElementById("newNome").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newAnaemia").value = "";
  document.getElementById("newCreatinine_phosphokinase").value = "";
  document.getElementById("newDiabetes").value = "";
  document.getElementById("newEjection_fraction").value = "";
  document.getElementById("newHigh_blood_pressure").value = "";
  document.getElementById("newPlatelets").value = "";
  document.getElementById("newSerum_creatinine").value = "";
  document.getElementById("newSerum_sodium").value = "";
  document.getElementById("newSex").value = "";
  document.getElementById("newSmoking").value = "";
  document.getElementById("newTime").value = ""; 


  removeElement()
}



/*
  --------------------------------------------------------------------------------------
  Função para limpar o formulário
  --------------------------------------------------------------------------------------
*/
function limparForm(){
  document.getElementById("newNome").value = "";
  document.getElementById("newAge").value = "";
  document.getElementById("newAnaemia").value = "";
  document.getElementById("newCreatinine_phosphokinase").value = "";
  document.getElementById("newDiabetes").value = "";
  document.getElementById("newEjection_fraction").value = "";
  document.getElementById("newHigh_blood_pressure").value = "";
  document.getElementById("newPlatelets").value = "";
  document.getElementById("newSerum_creatinine").value = "";
  document.getElementById("newSerum_sodium").value = "";
  document.getElementById("newSex").value = "";
  document.getElementById("newSmoking").value = "";
  document.getElementById("newTime").value = ""; 
}

/*
  --------------------------------------------------------------------------------------
  Chamada de funções para carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
limparForm();

/*
  --------------------------------------------------------------------------------------
  Função para deletar um item da lista do servidor via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (item) => {
  console.log(item)
  let url = 'http://127.0.0.1:5000/paciente?id=' + item;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Bloco de funções feito em jQuery
  --------------------------------------------------------------------------------------
*/
jQuery(document).ready(function() {

  //variavel global para guardar o id do alimento que será excluido
  var idDel = 0;

  /*
  --------------------------------------------------------------------------------------
  Função para editar um item da lista de acordo com o click no botão update
  --------------------------------------------------------------------------------------
  */
  $('#myTable tbody').on('click', '.linkEdit', function () {
    var table = $('#myTable').DataTable();
    var tr = $(this).closest('tr');
    var data = table.row(tr).data();
    
    $("#newid").val(data.id);
    $("#newNome").val(data.name);
    $("#newAge").val(data.age);
    $("#newAnaemia").val(data.anae);
    $("#newCreatinine_phosphokinase").val(data.crea);
    $("#newDiabetes").val(data.diab);        
    $("#newEjection_fraction").val(data.ejec);        
    $("#newHigh_blood_pressure").val(data.high);        
    $("#newPlatelets").val(data.plate);        
    $("#newSerum_creatinine").val(data.ser_crea);        
    $("#newSerum_sodium").val(data.ser_sodi);        
    $("#newSex").val(data.sex);        
    $("#newSmoking").val(data.smok);        
    $("#newTime").val(data.tim);            
    
    
    $("#butSubmit").text("atualizar");  
    $("#butSubmit").val("atualizar");    
    $("#newType").val("atualizar");    
    
    $("#divButCancelar").show();    
    
  });

  /*
  --------------------------------------------------------------------------------------
  Função para incluir ou atualizar um item de acordo com o click do mouse
  --------------------------------------------------------------------------------------
  */
  $('#butSubmit').click(function() {                

    let inputTipo = document.getElementById("butSubmit").value;
    let inputId = document.getElementById("newid").value;
    let inputNome = document.getElementById("newNome").value;
    let inputAge = document.getElementById("newAge").value;
    let inputAnemia = document.getElementById("newAnaemia").value;
    let inputCreatina = document.getElementById("newCreatinine_phosphokinase").value;
    let inputDiabetes = document.getElementById("newDiabetes").value;
    let inputEjection = document.getElementById("newEjection_fraction").value;
    let inputBlood = document.getElementById("newHigh_blood_pressure").value;
    let inputPlaqueta = document.getElementById("newPlatelets").value;
    let inputCreatinaSerum = document.getElementById("newSerum_creatinine").value;
    let inputSodio = document.getElementById("newSerum_sodium").value;
    let inputSex = document.getElementById("newSex").value;
    let inputSmoking = document.getElementById("newSmoking").value;
    let inputTime = document.getElementById("newTime").value; 
    
    var msg = '';
    if (inputNome === '') {
      msg += "Escreva o nome do paciente!\n";    
    } 
    if (inputAge === '') {
      msg += "Escreva a idade do paciente!\n";    
    }else{
      if (isNaN(inputAge)) {
        msg += "Idade precisa ser número!\n";
      }
    }
    if (inputAnemia === '') {
      msg += "Escreva se já teve ou tem anemia!\n";    
    }else{
      if (isNaN(inputAnemia)) {
        msg += "Anemia precisa ser número!\n";
      }
    }
    if (inputCreatina === '') {
      msg += "Escreva o valor da creatina fosfoquinase!\n";    
    }else{
      if (isNaN(inputCreatina)) {
        msg += "Creatina fosfoquinase precisa ser número!\n";
      }
    }
    if (inputDiabetes === '') {
      msg += "Escreva se tem diabetes!\n";    
    }else{
      if (isNaN(inputDiabetes)) {
        msg += "Diabetes precisa ser número!\n";
      }
    }   

    if (inputEjection === '') {
      msg += "Escreva o valor da fração de ejeção!\n";    
    }else{
      if (isNaN(inputEjection)) {
        msg += "Fração de ejeção precisa ser número!\n";
      }
    }
    if (inputBlood === '') {
      msg += "Escreva se tem pressão sanguínea alta!\n";    
    }else{
      if (isNaN(inputBlood)) {
        msg += "Pressão sanguínea alta precisa ser número!\n";
      }
    }
    if (inputPlaqueta === '') {
      msg += "Escreva o valor das plaquetas!\n";    
    }else{
      if (isNaN(inputPlaqueta)) {
        msg += "Plaquetas precisa ser número!\n";
      }
    }
    if (inputCreatinaSerum === '') {
      msg += "Escreva o valor creatinina sérica!\n";    
    }else{
      if (isNaN(inputCreatinaSerum)) {
        msg += "Creatinina sérica precisa ser número!\n";
      }
    }
    if (inputSodio === '') {
      msg += "Escreva o valor do sódio!\n";    
    }else{
      if (isNaN(inputSodio)) {
        msg += "Sódio precisa ser número!\n";
      }
    }
    if (inputSex === '') {
      msg += "Escreva o sexo!\n";    
    }else{
      if (isNaN(inputSex)) {
        msg += "Sexo precisa ser número!\n";
      }
    }
    if (inputSmoking === '') {
      msg += "Escreva se fuma!\n";    
    }else{
      if (isNaN(inputSmoking)) {
        msg += "Fuma precisa ser número!\n";
      }
    }
    if (inputTime === '') {
      msg += "Escreva o tempo!\n";    
    }else{
      if (isNaN(inputTime)) {
        msg += "Tempo precisa ser número!\n";
      }
    }
    
  
    if(msg!=''){
      alert(msg);    
    }
    else
    { 
      if(inputTipo=='cadastrar'){
                
        /*
          --------------------------------------------------------------------------------------
          Função para incluir um item na lista do servidor via requisição POST
          --------------------------------------------------------------------------------------
        */
        var postForm = { //Fetch form data
          'name'         : inputNome,
          'age'          : inputAge,
          'anae'         : inputAnemia,
          'crea'         : inputCreatina,
          'diab'         : inputDiabetes,
          'ejec'         : inputEjection,
          'high'         : inputBlood,
          'plate'        : inputPlaqueta,
          'ser_crea'     : inputCreatinaSerum,
          'ser_sodi'     : inputSodio,
          'sex'          : inputSex,
          'smok'         : inputSmoking,
          'tim'         : inputTime          

        };
        


        $.ajax({
          type: "post",
          url: 'http://127.0.0.1:5000/paciente',    
          data: postForm,  
          success: function(result){
            alert("Item adicionado!")
            location.reload();
          },
          error: function(jqXHR, textStatus, errorThrown) {
            var status = jqXHR.status;
            //var msg = jqXHR.responseText;
             console.log(textStatus, errorThrown);             
              switch (status) {
                case 400: //Bad Request
                  alert("Bad Request");                  
                case 409: //conflict                  
                  alert("Paciente de mesmo nome já salvo na base");                  
                case 422: //Unprocessable Entity
                  //alert("Unprocessable Entity");                  
                default: //Unknown server error occured
                  throw new Error(`Unknown server error occured:`+ textStatus);
              }
          }
        });
      
       
      }else{ //atualizar

        /*
          --------------------------------------------------------------------------------------
          Função para atualizar um item na lista do servidor via requisição POST
          --------------------------------------------------------------------------------------
        */
        var postForm = { //Fetch form data
          'id'           : inputId,          
          'name'         : inputNome,
          'age'          : inputAge,
          'anae'         : inputAnemia,
          'crea'         : inputCreatina,
          'diab'         : inputDiabetes,
          'ejec'         : inputEjection,
          'high'         : inputBlood,
          'plate'        : inputPlaqueta,
          'ser_crea'     : inputCreatinaSerum,
          'ser_sodi'     : inputSodio,
          'sex'          : inputSex,
          'smok'         : inputSmoking,
          'tim'          : inputTime         
        };
        

        $.ajax({
          type: "post",
          url: 'http://127.0.0.1:5000/update_paciente',    
          data: postForm,  
          success: function(result){
            alert("Item Atualizado!")
            $("#newType").val("cadastrar");   
            $("#newid").val("");   
            location.reload();
          },
          error: function(jqXHR, textStatus, errorThrown) {
            var status = jqXHR.status;
            //var msg = jqXHR.responseText;
            console.log(textStatus, errorThrown);             
              switch (status) {
                case 400: //Bad Request
                  alert("Bad Request");                  
                case 409: //conflict                  
                  alert("Paciente de mesmo nome já salvo na base");                  
                case 422: //Unprocessable Entity
                  alert("Unprocessable Entity");                  
                default: //Unknown server error occured
                  throw new Error(`Unknown server error occured:`+ textStatus);
              }
          }
        });
      }
    }

  });

  /*
  --------------------------------------------------------------------------------------
  Função para cancelar o update
  --------------------------------------------------------------------------------------
  */
  $('#butCancelar').on('click', function () {	
    limparForm();
    $("#divButCancelar").hide(); 
    $("#butSubmit").text("cadastrar");  
    $("#newType").val("cadastrar");    
  });

  /*
  --------------------------------------------------------------------------------------
  Função para excluir 
  --------------------------------------------------------------------------------------
  */
  $('#myTable tbody').on('click', '.linkDelete', function () {				
    var table = $('#myTable').DataTable();
    var tr = $(this).closest('tr');
    var data = table.row(tr).data();
    idDel = data.id;   
    if (confirm("Você tem certeza que deseja excluir o paciente?")) {
      deleteItem(idDel);      
      alert("Paciente Removido!");            
      table.row( $(this).parents('tr') ).remove().draw();  
      idDel = 0;
    }
  });

  /*
  ----------------------------------------------------------------------------------------------
  Função para fazer uma requisição de alimentos por ajax via GET e preencher o objeto Datatable
  ----------------------------------------------------------------------------------------------
  */
  $.ajax({
    type: "GET",
    url: 'http://127.0.0.1:5000/pacientes',      
    success: function(result){
      $('#myTable').DataTable({       
          
        "ordering": true,
				"paging": true,
				"pagingType": "full_numbers",
				"pageLength": 10,
        "processing": true,				
        "aaData": result.pacientes,
        "columns": [                   
              { "data": 'id', title: "Id" },
              { "data": 'name', title: "Nome" },
              { "data": 'age', title: "Idade" },        
              { "data": 'anae', title: "Anemia" },
              { "data": 'crea', title: "Creatina Fosfoquinase" },
              { "data": 'diab', title: "Diabetes" },
              { "data": 'ejec', title: "Fração ejeção" },
              { "data": 'high', title: "Pressão sanguínes" },
              { "data": 'plate', title: "Plaquetas" },
              { "data": 'ser_crea', title: "Creatinina Sérica" },
              { "data": 'ser_sodi', title: "Sódio" },
              { "data": 'sex', title: "Sexo" },
              { "data": 'smok', title: "Fuma" },
              { "data": 'tim', title: "Tempo" },
              { "data": 'death', title: "Morte" },              
              {
                "data": "edit",						
                "bSearchable": false,
                "bSortable": false,
                "render": function (data, type, row) {							
                  return '<a href="#" class="linkEdit"><img src="img/pencil.png" width="15px" height="15px"></i></a>';
                  
                }
              },
              {
                "data": "delete",						
                "bSearchable": false,
                "bSortable": false,
                "render": function (data, type, row) {							
                  return '<a href="#" class="linkDelete"><img src="img/excluir.png" width="15px" height="15px"></i></a>';							
                }
              }              
        ]            
      });
    }
  });

});

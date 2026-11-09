<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temperature Converter</title>
    <style>
        body {
            text-align: center;
            background: linear-gradient(135deg, rgb(217, 255, 0), rgb(255, 183, 0));
            background-repeat: no-repeat;
            margin-top:300px;
            height: 1000px;
            overflow: hidden;
        }
        #entrybox {
            border: 2px solid;
            border-radius: 5px; 
            margin: auto;
            width: 300px;
            padding: 26px;
            background: linear-gradient(135deg, rgb(45, 234, 11), rgb(79, 195, 71));
        }
        p {
            margin: 0;
        }
        #enterMsg{
            margin-bottom: 10px;
            font-size: 20px;
        }
        #input{
            height:50px;
            width:100px;
            border: 2px solid;
            border-radius: 10px;
            text-align: center;
            font-size:30px;
        }
        #convert{
            height:56px;
            border: 2px solid;
            border-radius: 10px;
            position: relative;
            top: -3px;
            margin-left:5px;
            font-size: 20px;
            font-weight:800;
            padding:15px;
        }

    </style>
</head>
<body>
    <h1>Temperature Converter</h1>
    <div id="entrybox">
        <p id="enterMsg">Please enter temperature in °F: </p>
        <input id="input" type="number" placeholder="°F">
        <button id="convert" onclick="convert()">convert</button>
    </div>
    <p id="output"></p>
</body>
<script type="text/javascript">
    const input = document.querySelector('#input');
    const convertBtn = document.querySelector('#convert');
    const output = document.querySelector('#output');

    function convert() {
        let F = input.value;
        if(!F){
            output.textContent = please enter a number;
            return;
        }
        F = parseFloat(F);
        const C = (F - 32) * 5 / 9;
        output.textContent = temperature in °C: ${C.toFixed(2)};
    };
</script>
</html>

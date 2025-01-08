/*
En este proyecto, desarrollo una calculadora funcional con las operaciones aritméticas básicas, 
implementando conceptos básicos como funciones, variables, operaciones
aritméticas, estructuras de control y de repetición (bucles), obtener datos del teclado y mostrar resultados en pantalla.

Este proyecto es parte de una serie de aplicaciones que estaré desarrollando en diferentes lenguajes de programación para mejorar la lógica y extender mis habilidades como programador y hacker.

Att: Kevin Feliz Henríquez.
*/

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function suma(a, b) {
    return a + b;
}

function resta(a, b) {
    return a - b;
}

function multiplicacion(a, b) {
    return a * b;
}

function division(a, b) {
    if (b === 0) {
        return "Error: División entre cero no permitida.";
    }
    return a / b;
}

function obtenerEntrada(prompt) {
    return new Promise((resolve) => rl.question(prompt, resolve));
}

async function calculadora() {
    console.log("Bienvenido a la Calculadora");

    while (true) {
        console.log("\nSeleccione una operación:");
        console.log("1. Suma");
        console.log("2. Resta");
        console.log("3. Multiplicación");
        console.log("4. División");
        console.log("5. Salir");

        const opcion = parseInt(await obtenerEntrada("Ingrese su opción: "));

        if (opcion === 5) {
            console.log("Saliendo de la calculadora. ¡Adiós!");
            rl.close();
            break;
        }

        if (![1, 2, 3, 4].includes(opcion)) {
            console.log("Opción no válida. Inténtelo de nuevo.");
            continue;
        }

        const num1 = parseFloat(await obtenerEntrada("Ingrese el primer número: "));
        const num2 = parseFloat(await obtenerEntrada("Ingrese el segundo número: "));

        if (isNaN(num1) || isNaN(num2)) {
            console.log("Por favor, ingrese números válidos.");
            continue;
        }

        let resultado;
        switch (opcion) {
            case 1:
                resultado = suma(num1, num2);
                break;
            case 2:
                resultado = resta(num1, num2);
                break;
            case 3:
                resultado = multiplicacion(num1, num2);
                break;
            case 4:
                resultado = division(num1, num2);
                break;
        }
        console.log(`Resultado: ${resultado}`);
    }
}

calculadora();

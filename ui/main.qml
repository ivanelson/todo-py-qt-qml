import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 500
    height: 600
    title: "Cadastro de Tarefas"

    property bool titleError: false
    property bool taskNameError: false

    Column {
        anchors.centerIn: parent
        spacing: 10

        TextField {
            id: inputId
            visible: false
        }

        TextField {
            id: inputTitle
            placeholderText: "Título"
            border.color: titleError ? "red" : "lightgray"
            border.width: 1
        }

        TextField {
            id: inputName
            placeholderText: "Descrição da tarefa"
            border.color: taskNameError ? "red" : "lightgray"
            border.width: 1
        }

        ComboBox {
            id: statusCombo
            model: ["novo", "em andamento", "cancelada", "concluida"]
            currentIndex: 0
        }

        Row {
            spacing: 10
            Button {
                text: "Salvar Tarefa"
                onClicked: {
                    titleError = inputTitle.text.trim().length === 0
                    taskNameError = inputName.text.trim().length === 0
                    if (!titleError && !taskNameError) {
                        taskController.addTask(inputTitle.text, inputName.text, statusCombo.currentText)
                    }
                }
            }

            Button {
                text: "Atualizar Tarefa"
                onClicked: {
                    if (inputId.text.trim().length > 0) {
                        taskController.updateTask(parseInt(inputId.text), inputTitle.text, inputName.text, statusCombo.currentText)
                    }
                }
            }
        }

        Row {
            spacing: 10
            ComboBox {
                id: filterCombo
                model: ["", "novo", "em andamento", "cancelada", "concluida"]
                currentIndex: 0
                width: 200
                displayText: currentText.length > 0 ? "Filtrar: " + currentText : "Sem filtro"
            }

            Button {
                text: "Aplicar Filtro"
                onClicked: taskController.filterTasks(filterCombo.currentText)
            }

            Button {
                text: "Limpar Filtro"
                onClicked: taskController.filterTasks("")
            }
        }

        ListView {
            width: parent.width
            height: 200
            model: taskController.getTaskList()
            delegate: Rectangle {
                width: parent.width
                height: 50
                border.width: 1
                border.color: "gray"
                Text {
                    text: "[" + model.status + "] " + model.title + ": " + model.task_name
                    anchors.centerIn: parent
                }
                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        inputId.text = model.id
                        inputTitle.text = model.title
                        inputName.text = model.task_name
                        statusCombo.currentIndex = statusCombo.find(model.status)
                    }
                }
            }
        }

        Dialog {
            id: errorDialog
            title: "Erro"
            standardButtons: Dialog.Ok
            visible: false

            Text {
                id: errorText
                text: ""
            }
        }
    }

    Connections {
        target: taskController
        function onErrorOccurred(message) {
            errorText.text = message
            errorDialog.open()
        }
    }
}
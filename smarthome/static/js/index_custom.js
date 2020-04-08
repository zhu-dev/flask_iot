//定义全局变量，标记当前房间
var room_status = "parlour";

//页面加载就绪后，请求数据
$(document).ready(function () {
    getData('parlour')
});

/**
 * checkbox监听事件
 * @param obj
 * @param method
 */
function onChangeHandle(obj, method) {
    if (obj.checked) {
        //打开
        commands(method, true);
        console.log("open")
    } else {
        //关闭
        commands(method, false);
        console.log("close")
    }

}

/**
 * 房间选择点击事件监听
 * @param room
 */
function onClickHandle(room) {
    room_status = room;
    //请求数据
    getData(room);
    console.log("click")
}

/**
 * 命令组装分发
 * @param method
 * @param isOpen
 */
function commands(method, isOpen) {
    switch (method) {
        case "parlour_light":
            if (isOpen == true) {
                json_data = {"method": "lighting_parlour", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "lighting_parlour", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
        case "bedroom_light":
            if (isOpen == true) {
                json_data = {"method": "lighting_bedroom", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "lighting_bedroom", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
        case "kitchen_light":
            if (isOpen == true) {
                json_data = {"method": "lighting_kitchen", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "lighting_kitchen", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
        case "curtain":
            if (isOpen == true) {
                json_data = {"method": "curtain", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "curtain", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
        case "fan":
            if (isOpen == true) {
                json_data = {"method": "fanning", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "fanning", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
        case "extend":
            if (isOpen == true) {
                json_data = {"method": "extend_other", "paras": {"open": "O"}};
                sendCommand(json_data)
            } else {
                json_data = {"method": "extend_other", "paras": {"open": "C"}};
                sendCommand(json_data)
            }
            break;
    }
}

/**
 * 发送命令
 * @param json_data
 */
function sendCommand(json_data) {
    $.ajax({
        url: 'http://127.0.0.1:5000/commands',
        type: "POST",
        dataType: "json",
        data: json_data,
        success: function (data) {
            console.log("sendCommand success")
        }
    })
}

/**
 * 获取房间数据
 * @param room
 */
function getData(room) {
    $.ajax({
        url: 'http://127.0.0.1:5000/home_datas',
        type: "GET",
        dataType: "json",
        data: {room: room},
        success: function (data) {
            if (data.code == 2) {
                console.log(data.data);
                updateData(data.data)
            } else {
                console.log(data.message);
            }
        }
    })
}

/**
 * 将数据更新到三个曲线
 * @param results
 */
function updateData(results) {

    var labels_list = [];
    var temperature_list = [];
    var humidity_list = [];
    var smoke_list = [];
    var time_label = null;

    for (data of results) {
        time_label = data.time.substr(11);
        labels_list.push(time_label);
        temperature_list.push(data.temperature);
        humidity_list.push(data.humidity);
        smoke_list.push(data.smoke);
    }
    var data1 = {
        //labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        labels: labels_list.reverse(),
        datasets: [
            {
                label: "My Second dataset",
                fillColor: "rgba(151,187,205,0.2)",
                strokeColor: "rgba(151,187,205,1)",
                pointColor: "rgba(151,187,205,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: temperature_list.reverse()
            }
        ]
    }
    var data2 = {
        //labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        labels: labels_list.reverse(),
        datasets: [
            {
                label: "My Second dataset",
                fillColor: "rgba(151,187,205,0.2)",
                strokeColor: "rgba(151,187,205,1)",
                pointColor: "rgba(151,187,205,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: humidity_list.reverse()
            }
        ]
    }
    var data3 = {
        //labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
        labels: labels_list.reverse(),
        datasets: [
            {
                label: "My Second dataset",
                fillColor: "rgba(151,187,205,0.2)",
                strokeColor: "rgba(151,187,205,1)",
                pointColor: "rgba(151,187,205,1)",
                pointStrokeColor: "#fff",
                pointHighlightFill: "#fff",
                pointHighlightStroke: "rgba(151,187,205,1)",
                data: smoke_list.reverse()
            }
        ]
    };
    var lineChartConf = {
        scaleStartValue: null
    };

    var ctxl = $("#lineChartDemo").get(0).getContext("2d");
    var lineChart = new Chart(ctxl).Line(data1, lineChartConf);

    var ctxl2 = $("#lineChartDemo2").get(0).getContext("2d");
    var lineChart2 = new Chart(ctxl2).Line(data2);

    var ctxl3 = $("#lineChartDemo3").get(0).getContext("2d");
    var lineChart3 = new Chart(ctxl3).Line(data3);
}


//定时请求更新数据
window.setInterval(updateInterval, 7000);

/**
 * 定时更新数据
 */
function updateInterval() {
    $.ajax({
        url: 'http://127.0.0.1:5000/home_datas',
        type: "GET",
        dataType: "json",
        data: {room: room_status},
        success: function (data) {
            if (data.code == 2) {
                console.log(data.data);
                updateData(data.data)
            } else {
                console.log(data.message);
            }
        }
    })
}
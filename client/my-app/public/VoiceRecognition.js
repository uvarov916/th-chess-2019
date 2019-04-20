var dict = new ya.speechkit.SpeechRecognition();
var tts_stream = new ya.speechkit.Tts({errorCallback: console.log});
tts_stream.speakers();

function startListen(dataCallback) {
    var apikey = "069b6659-984b-4c5f-880e-aaedcfd84102";
    var uuid = ya.speechkit.settings.uuid;
    var deviceuuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(
        /[xy]/g,
        function (c) {
            var r = Math.random() * 16 | 0;
            var v = c == 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        }
    );
    var modelValue = 'notes';
    var formatValue = "OPUS";
    var langValue = 'ru-RU';
    var format = ya.speechkit.FORMAT[formatValue];
    dict.start({
        apikey: apikey,
        uuid: uuid,
        yandexuid: "",
        biometry_group: deviceuuid,
        model: modelValue,
        applicationName: 'sandbox',
        lang: langValue,
        format: format,
        errorCallback: function (msg) {
            console.log(msg);
        },
        dataCallback: function(text, uttr) {
            if(uttr) {
                console.log(text);
                if(dataCallback) {
                    dataCallback.call(window, text);
                }
            }
        },
        infoCallback: function (info) {
            // console.log('info: ');
            // console.log(info);
        },
        customGrammar:  [],
        srgs:  undefined,
        capitalize: false,
        expNumCount: 0,
        allowStrongLanguage: true,
        allowMultiUtterance: true,
        punctuation: true,
        manualPunctuation: false,
        partialResults: true,
        utteranceSilence: 120,
        cmnWindow: 600,
        cmnLatency: 150,
        chunkProcessLimit: 500,
        biometry: "",
        use_snr: false,
        snr_flags: ""
    });
};


function speakWords(words) {
    tts_stream.speak(words, {
        lang: "ru-RU",
        voice: "oksana",
        emotion: '',
        speed: '',
        volume: "1.0",
        quality: "ultra",
        apikey: "069b6659-984b-4c5f-880e-aaedcfd84102",
        engine: "ytcp2",
        dataCallback: function(blob) {
            var el = document.getElementById('audio-player');
            el.src = URL.createObjectURL(blob);
            el.play();
        },
        infoCallback: function(){
        },
        errorCallback: function(err){
        }
    });
}

window.startListen = startListen;
window.stopListen = function() {
    dict.stop();
}
window.speakWords = speakWords;

// document.getElementById('pause_btn').onclick = dict.pause.bind(dict);
// document.getElementById('stop_btn').onclick = dict.stop.bind(dict);


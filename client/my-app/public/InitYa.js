(function (namespace) {
    'use strict';
    if (typeof namespace.ya === 'undefined') {
        namespace.ya = {};
    }
    if (typeof namespace.ya.speechkit === 'undefined') {
        namespace.ya.speechkit = {};
    }
    namespace.ya.speechkit.settings = {
        websocketProtocol: 'wss://',
        asrUrl: 'webasr.yandex.net' + '/asrsocket.ws',
        ttsStreamUrl: 'webasr.yandex.net' + '/ttssocket.ws',
        ttsUrl: 'http://tts.voicetech.yandex.net',
        apikey: '',
        uuid: 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(
            /[xy]/g,
            function (c) {
                var r = Math.random() * 16 | 0;
                var v = c == 'x' ? r : (r & 0x3 | 0x8);
                return v.toString(16);
            }
        ),
        model: 'notes',
        lang: 'ru-RU',
        langWhitelist: ['ru-RU', 'en-US', 'tr-TR', 'uk-UA', 'ru', 'en', 'tr', 'de', 'uk', 'es', 'it', 'it-IT', 'en-GB', 'en-EN', 'es-ES', 'fr-FR', 'de-DE'],
        voicelabUrl: 'https://voicelab.voicetech.yandex.net/',
        mdsDownloadUrl: 'https://storage.mds.yandex.net/get-phrase-spotter/',
        modelCreatorUrl: 'https://model-creator.yandex.net/',
    };
})(this);

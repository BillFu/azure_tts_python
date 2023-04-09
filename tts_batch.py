# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.


import azure.cognitiveservices.speech as speechsdk
import sys


speech_key, service_region = "0b4f6b5870ec4cefa3bdf12f73862a32", "eastasia"


# Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
# "zh-CN-YunfengNeural"


def synth_one_clip(text_to_synth, out_audio_file, voice_name):
    # Creates an instance of a speech config with specified subscription key and service region.
    # Replace with your own subscription key and service region (e.g., "westus").
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    speech_config.speech_synthesis_voice_name = voice_name

    audio_config = speechsdk.audio.AudioOutputConfig(filename=out_audio_file)

    # Creates a speech synthesizer using the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Synthesizes the received text to speech.
    # The synthesized speech is expected to be heard on the speaker with this line executed.
    result = speech_synthesizer.speak_text_async(text_to_synth).get()

    # Checks result.
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized to speaker for text [{}]".format(text_to_synth))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
        print("Did you update the subscription info?")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise ValueError('Please provide email-id to send the email.')
        print("Correct Usage: python tts_batch.py in_text out_wav")
        exit(0)

    # print(f'--Script Name is {sys.argv[0]}')

    in_text = sys.argv[1]
    print(f'input text: {in_text}')
    out_wav = sys.argv[2]
    print(f'output wav file: {out_wav}')

    # voice_name = "zh-CN-YunfengNeural"
    voice_name = "zh-CN-shaanxi-XiaoniNeural"
    # zh - CN - shaanxi - XiaoniNeural
    synth_one_clip(in_text, out_wav, voice_name)

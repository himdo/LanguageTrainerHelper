from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none
# import time
import torch

class Languages:
    Japanese = 'Japanese'
    English = 'English'
    Mandarin = 'Mandarin'
    
class TextToSpeech:
    def __init__(self, language):
        if language == Languages.Japanese:
            #@title Choose Japanese model { run: "auto" }
            self.lang = 'Japanese'
            self.tag = 'kan-bayashi/jsut_full_band_vits_prosody' #@param ["kan-bayashi/jsut_tacotron2", "kan-bayashi/jsut_transformer", "kan-bayashi/jsut_fastspeech", "kan-bayashi/jsut_fastspeech2", "kan-bayashi/jsut_conformer_fastspeech2", "kan-bayashi/jsut_conformer_fastspeech2_accent", "kan-bayashi/jsut_conformer_fastspeech2_accent_with_pause", "kan-bayashi/jsut_vits_accent_with_pause", "kan-bayashi/jsut_full_band_vits_accent_with_pause", "kan-bayashi/jsut_tacotron2_prosody", "kan-bayashi/jsut_transformer_prosody", "kan-bayashi/jsut_conformer_fastspeech2_tacotron2_prosody", "kan-bayashi/jsut_vits_prosody", "kan-bayashi/jsut_full_band_vits_prosody", "kan-bayashi/jvs_jvs010_vits_prosody", "kan-bayashi/tsukuyomi_full_band_vits_prosody"] {type:"string"}
            self.vocoder_tag = 'none' #@param ["none", "parallel_wavegan/jsut_parallel_wavegan.v1", "parallel_wavegan/jsut_multi_band_melgan.v2", "parallel_wavegan/jsut_style_melgan.v1", "parallel_wavegan/jsut_hifigan.v1"] {type:"string"}

        elif language == Languages.English:
            #@title Choose English model { run: "auto" }
            self.lang = 'English'
            self.tag = 'kan-bayashi/ljspeech_vits' #@param ["kan-bayashi/ljspeech_tacotron2", "kan-bayashi/ljspeech_fastspeech", "kan-bayashi/ljspeech_fastspeech2", "kan-bayashi/ljspeech_conformer_fastspeech2", "kan-bayashi/ljspeech_joint_finetune_conformer_fastspeech2_hifigan", "kan-bayashi/ljspeech_joint_train_conformer_fastspeech2_hifigan", "kan-bayashi/ljspeech_vits"] {type:"string"}
            self.vocoder_tag = "none" #@param ["none", "parallel_wavegan/ljspeech_parallel_wavegan.v1", "parallel_wavegan/ljspeech_full_band_melgan.v2", "parallel_wavegan/ljspeech_multi_band_melgan.v2", "parallel_wavegan/ljspeech_hifigan.v1", "parallel_wavegan/ljspeech_style_melgan.v1"] {type:"string"}

        elif language == Languages.Mandarin:
            #@title Choose Mandarin model { run: "auto" }
            self.lang = 'Mandarin'
            self.tag = 'kan-bayashi/csmsc_full_band_vits' #@param ["kan-bayashi/csmsc_tacotron2", "kan-bayashi/csmsc_transformer", "kan-bayashi/csmsc_fastspeech", "kan-bayashi/csmsc_fastspeech2", "kan-bayashi/csmsc_conformer_fastspeech2", "kan-bayashi/csmsc_vits", "kan-bayashi/csmsc_full_band_vits"] {type: "string"}
            self.vocoder_tag = "none" #@param ["none", "parallel_wavegan/csmsc_parallel_wavegan.v1", "parallel_wavegan/csmsc_multi_band_melgan.v2", "parallel_wavegan/csmsc_hifigan.v1", "parallel_wavegan/csmsc_style_melgan.v1"] {type:"string"}


        self.text2speech = Text2Speech.from_pretrained(
            model_tag=str_or_none(self.tag),
            vocoder_tag=str_or_none(self.vocoder_tag),
            device="cuda",
            # Only for Tacotron 2 & Transformer
            threshold=0.5,
            # Only for Tacotron 2
            minlenratio=0.0,
            maxlenratio=10.0,
            use_att_constraint=False,
            backward_window=1,
            forward_window=3,
            # Only for FastSpeech & FastSpeech2 & VITS
            speed_control_alpha=1.0,
            # Only for VITS
            noise_scale=0.333,
            noise_scale_dur=0.333,
        )

    def Generate(self, text, outputDir):
        # synthesis
        with torch.no_grad():
            wav = self.text2speech(text)["wav"]

        from scipy.io.wavfile import write
        write(outputDir, self.text2speech.fs, wav.view(-1).cpu().numpy())
        return True

# t2s = TextToSpeech(Languages.Japanese)
# t2s.Generate('こんにちは 試運転です', 'a.wav')
from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import torch

app = Flask(__name__)

tran = pipeline("translation", model="facebook/nllb-200-1.3B",
                torch_dtype=torch.bfloat16)

LANGUAGES = {
    "ace_Arab": "Achinese (Arabic script)",
    "ace_Latn": "Achinese (Latin script)",
    "acm_Arab": "Mesopotamian Arabic",
    "acq_Arab": "Ta'izzi-Adeni Arabic",
    "aeb_Arab": "Tunisian Arabic",
    "afr_Latn": "Afrikaans",
    "ajp_Arab": "South Levantine Arabic",
    "aka_Latn": "Akan",
    "amh_Ethi": "Amharic",
    "apc_Arab": "North Levantine Arabic",
    "arb_Arab": "Standard Arabic",
    "ars_Arab": "Najdi Arabic",
    "ary_Arab": "Moroccan Arabic",
    "arz_Arab": "Egyptian Arabic",
    "asm_Beng": "Assamese",
    "ast_Latn": "Asturian",
    "awa_Deva": "Awadhi",
    "ayr_Latn": "Aymara",
    "azb_Arab": "South Azerbaijani",
    "azj_Latn": "North Azerbaijani",
    "bak_Cyrl": "Bashkir",
    "bam_Latn": "Bambara",
    "ban_Latn": "Balinese",
    "bel_Cyrl": "Belarusian",
    "bem_Latn": "Bemba",
    "ben_Beng": "Bengali",
    "bho_Deva": "Bhojpuri",
    "bjn_Arab": "Banjar (Arabic script)",
    "bjn_Latn": "Banjar (Latin script)",
    "bod_Tibt": "Tibetan",
    "bos_Latn": "Bosnian",
    "bug_Latn": "Buginese",
    "bul_Cyrl": "Bulgarian",
    "cat_Latn": "Catalan",
    "ceb_Latn": "Cebuano",
    "ces_Latn": "Czech",
    "cjk_Latn": "Chokwe",
    "ckb_Arab": "Central Kurdish (Sorani)",
    "crh_Latn": "Crimean Tatar",
    "cym_Latn": "Welsh",
    "dan_Latn": "Danish",
    "deu_Latn": "German",
    "dik_Latn": "Dinka",
    "dyu_Latn": "Dyula",
    "dzo_Tibt": "Dzongkha",
    "ell_Grek": "Greek",
    "eng_Latn": "English",
    "epo_Latn": "Esperanto",
    "est_Latn": "Estonian",
    "eus_Latn": "Basque",
    "ewe_Latn": "Ewe",
    "fao_Latn": "Faroese",
    "pes_Arab": "Western Persian",
    "fij_Latn": "Fijian",
    "fin_Latn": "Finnish",
    "fon_Latn": "Fon",
    "fra_Latn": "French",
    "fur_Latn": "Friulian",
    "fuv_Latn": "Nigerian Fulfulde",
    "gla_Latn": "Scottish Gaelic",
    "gle_Latn": "Irish",
    "glg_Latn": "Galician",
    "grn_Latn": "Guarani",
    "guj_Gujr": "Gujarati",
    "hat_Latn": "Haitian Creole",
    "hau_Latn": "Hausa",
    "heb_Hebr": "Hebrew",
    "hin_Deva": "Hindi",
    "hne_Deva": "Chhattisgarhi",
    "hrv_Latn": "Croatian",
    "hun_Latn": "Hungarian",
    "hye_Armn": "Armenian",
    "ibo_Latn": "Igbo",
    "ilo_Latn": "Ilocano",
    "ind_Latn": "Indonesian",
    "isl_Latn": "Icelandic",
    "ita_Latn": "Italian",
    "jav_Latn": "Javanese",
    "jpn_Jpan": "Japanese",
    "kab_Latn": "Kabyle",
    "kan_Knda": "Kannada",
    "kas_Arab": "Kashmiri (Arabic script)",
    "kas_Deva": "Kashmiri (Devanagari script)",
    "kat_Geor": "Georgian",
    "kaz_Cyrl": "Kazakh",
    "khm_Khmr": "Khmer",
    "kin_Latn": "Kinyarwanda",
    "kir_Cyrl": "Kyrgyz",
    "kor_Hang": "Korean",
    "lao_Laoo": "Lao",
    "lit_Latn": "Lithuanian",
    "lug_Latn": "Ganda",
    "mal_Mlym": "Malayalam",
    "mar_Deva": "Marathi",
    "mkd_Cyrl": "Macedonian",
    "mlt_Latn": "Maltese",
    "mri_Latn": "Maori",
    "mya_Mymr": "Burmese",
    "nld_Latn": "Dutch",
    "nob_Latn": "Norwegian Bokmål",
    "pol_Latn": "Polish",
    "por_Latn": "Portuguese",
    "ron_Latn": "Romanian",
    "rus_Cyrl": "Russian",
    "sin_Sinh": "Sinhala",
    "slk_Latn": "Slovak",
    "slv_Latn": "Slovenian",
    "spa_Latn": "Spanish",
    "swe_Latn": "Swedish",
    "tam_Taml": "Tamil",
    "tel_Telu": "Telugu",
    "tha_Thai": "Thai",
    "tir_Ethi": "Tigrinya",
    "tur_Latn": "Turkish",
    "ukr_Cyrl": "Ukrainian",
    "urd_Arab": "Urdu",
    "uzn_Latn": "Uzbek",
    "vie_Latn": "Vietnamese",
    "xho_Latn": "Xhosa",
    "yor_Latn": "Yoruba",
    "zho_Hans": "Chinese (Simplified)",
    "zho_Hant": "Chinese (Traditional)",
    "zul_Latn": "Zulu"
}


@app.route('/')
def home():
    return render_template('index.html', languages=LANGUAGES)


@app.route('/translate', methods=['POST'])
def translate():
    # get user input
    src_lang = request.form.get('src_lang')
    tgt_lang = request.form.get('tgt_lang')
    text = request.form.get('text')

    # find the language codes
    for key, val in LANGUAGES.items():
        if val == src_lang:
            src_lang = key
        if val == tgt_lang:
            tgt_lang = key

    # do translation
    try:
        result = tran(text, src_lang=src_lang, tgt_lang=tgt_lang)
        translation = result[0]['translation_text']
        return jsonify({'translation': translation})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)

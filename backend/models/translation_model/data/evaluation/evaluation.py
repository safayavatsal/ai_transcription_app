def evaluate_model(translator, test_data):
    for src_sentence, tgt_sentence in test_data:
        translation = translator.translate(src_sentence)
        print(f"Source: {src_sentence}, Translation: {translation}, Target: {tgt_sentence}")

import 'package:flutter/material.dart';
import 'package:ai_transcription_app/services/api_service.dart';

class VoiceToTextComponent extends StatelessWidget {
  const VoiceToTextComponent({super.key});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () {
        ApiService().sendAudioFile();
      },
      child: const Text("Start Voice to Text"),
    );
  }
}

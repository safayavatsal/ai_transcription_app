import 'package:flutter/material.dart';
import 'package:ai_transcription_app/services/api_service.dart';

class TextToVoiceComponent extends StatelessWidget {
  final TextEditingController _controller = TextEditingController();

  TextToVoiceComponent({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        TextField(
          controller: _controller,
          decoration: const InputDecoration(
            labelText: "Enter text for speech",
          ),
        ),
        ElevatedButton(
          onPressed: () {
            ApiService().convertTextToVoice(_controller.text);
          },
          child: const Text("Convert to Voice"),
        ),
      ],
    );
  }
}

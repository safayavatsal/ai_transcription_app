import 'dart:io';
import 'package:http/http.dart' as http;

class ApiService {
  final String _baseUrl = 'https://your-api-endpoint.com'; // Cloud endpoint

  Future<void> sendAudioFile() async {
    // Capture and send audio data for voice-to-text processing
    final audioFile = File('path-to-audio-file');
    var request =
        http.MultipartRequest('POST', Uri.parse('$_baseUrl/voice-to-text'));
    request.files
        .add(await http.MultipartFile.fromPath('audio', audioFile.path));

    var response = await request.send();
    if (response.statusCode == 200) {
      print('Success');
    } else {
      print('Failed');
    }
  }

  Future<void> convertTextToVoice(String text) async {
    var response = await http.post(
      Uri.parse('$_baseUrl/text-to-voice'),
      headers: <String, String>{'Content-Type': 'application/json'},
      body: '{"text": "$text"}',
    );

    if (response.statusCode == 200) {
      print('Audio conversion successful');
    } else {
      print('Failed');
    }
  }
}

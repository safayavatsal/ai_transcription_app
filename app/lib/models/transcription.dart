class Transcription {
  final String text;
  final String language;
  final DateTime createdAt;

  Transcription({
    required this.text,
    required this.language,
    required this.createdAt,
  });

  Map<String, dynamic> toJson() {
    return {
      'text': text,
      'language': language,
      'createdAt': createdAt.toIso8601String(),
    };
  }

  factory Transcription.fromJson(Map<String, dynamic> json) {
    return Transcription(
      text: json['text'],
      language: json['language'],
      createdAt: DateTime.parse(json['createdAt']),
    );
  }
}

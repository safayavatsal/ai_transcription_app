class AudioSample {
  final String filePath;
  final String language;
  final DateTime timestamp;

  AudioSample({
    required this.filePath,
    required this.language,
    required this.timestamp,
  });

  Map<String, dynamic> toJson() {
    return {
      'filePath': filePath,
      'language': language,
      'timestamp': timestamp.toIso8601String(),
    };
  }

  factory AudioSample.fromJson(Map<String, dynamic> json) {
    return AudioSample(
      filePath: json['filePath'],
      language: json['language'],
      timestamp: DateTime.parse(json['timestamp']),
    );
  }
}

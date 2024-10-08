class TTSSettings {
  final String language;
  final double pitch;
  final double speed;

  TTSSettings({
    required this.language,
    required this.pitch,
    required this.speed,
  });

  Map<String, dynamic> toJson() {
    return {
      'language': language,
      'pitch': pitch,
      'speed': speed,
    };
  }

  factory TTSSettings.fromJson(Map<String, dynamic> json) {
    return TTSSettings(
      language: json['language'],
      pitch: json['pitch'],
      speed: json['speed'],
    );
  }
}

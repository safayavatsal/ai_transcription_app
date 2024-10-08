class TranslationResponse {
  final String translatedText;
  final bool success;
  final String errorMessage;

  TranslationResponse({
    required this.translatedText,
    required this.success,
    this.errorMessage = '',
  });

  Map<String, dynamic> toJson() {
    return {
      'translatedText': translatedText,
      'success': success,
      'errorMessage': errorMessage,
    };
  }

  factory TranslationResponse.fromJson(Map<String, dynamic> json) {
    return TranslationResponse(
      translatedText: json['translatedText'],
      success: json['success'],
      errorMessage: json['errorMessage'] ?? '',
    );
  }
}

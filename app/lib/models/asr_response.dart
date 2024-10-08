class ASRResponse {
  final String recognizedText;
  final bool success;
  final String errorMessage;

  ASRResponse({
    required this.recognizedText,
    required this.success,
    this.errorMessage = '',
  });

  Map<String, dynamic> toJson() {
    return {
      'recognizedText': recognizedText,
      'success': success,
      'errorMessage': errorMessage,
    };
  }

  factory ASRResponse.fromJson(Map<String, dynamic> json) {
    return ASRResponse(
      recognizedText: json['recognizedText'],
      success: json['success'],
      errorMessage: json['errorMessage'] ?? '',
    );
  }
}

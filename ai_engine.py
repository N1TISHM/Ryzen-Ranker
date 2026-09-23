import ollama  # type: ignore

class LocalInferenceEngine:
    """Manages text data summary maps natively for our small model constraints."""
    
    def __init__(self, model_name: str = "qwen2.5:0.5b"):
        self.model_name = model_name

    def _compile_context_summary(self, dataset_list: list) -> str:
        summary_lines = []
        for item in dataset_list:
            #  [LOCAL INTEL] Format native objects directly into clean string summaries
            summary_lines.append(
                f"- {item['Processor']}: Price ${item['Price']}, "
                f"Performance: {item['Performance']}/100, Value Index: {item['Value Score']}"
            )
        return "\n".join(summary_lines)

    def query_explainer(self, user_query: str, active_dataset: list) -> str:
        if not active_dataset:
            return "No active hardware options are currently visible to analyze."

        context = self._compile_context_summary(active_dataset)
        
        # [LOCAL INTEL] Rigid constraint prompt optimized for Qwen 0.5B limitations
        system_instruction = (
            "You are an expert PC hardware advisor analyzing an active AMD database.\n"
            "Contextual Matrix Data:\n"
            f"{context}\n\n"
            "Execution Instructions:\n"
            "1. Answer the question in 2-3 clean, punchy sentences.\n"
            "2. Ground your reasoning strictly in the numbers provided above.\n"
            "3. Be objective, precise, and professional."
        )

        try:
            #  [LOCAL INTEL] Execute local offline model text inference
            response = ollama.generate(
                model=self.model_name,
                prompt=f"{system_instruction}\n\nUser Inquiry: {user_query}"
            )
            return response.get('response', '').strip()
        except Exception as e:
            return f"Inference pipeline failure. Verify 'ollama run {self.model_name}' is active. Error: {e}"

        


# Build and render

Run `assets/build-smoke-test.tex` before deep extraction. Test the same language and mathematics required by the final deliverables. Record the command or tool, result, and diagnostics.

Choose the first backend that demonstrably works:

1. A harness-native LaTeX compiler, such as the Codex built-in compiler, when available.
2. An installed `latexmk`, `xelatex`, or equivalent engine proven by the smoke test.
3. The minimal template after removing optional styling packages or unsupported fonts.
4. A direct-PDF backend exposed by the active harness or an installed PDF skill, while preserving equivalent `.tex` sources.

Do not download TeX packages, fonts, or binaries without authorization. Do not use a remote renderer unless the user explicitly approves transmitting the content.

If all PDF paths fail, stop before full drafting and ask whether source-only delivery is acceptable. Continue only after explicit acceptance; label the result `PARTIAL`. If PDFs remain required, label the result `FAIL` and report the concrete missing capability.

After generation, render every PDF to page images and inspect it. Successful compilation alone does not pass visual QA.

On DeepSeek Harness, use only capabilities exposed by the active preset. If no image-inspection tool or multimodal model is available, require explicit manual-review or source-only acceptance and report `PARTIAL`; never infer visual correctness from extracted text.

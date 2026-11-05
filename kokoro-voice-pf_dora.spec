Name:		kokoro-voice-pf_dora
Version:	1.0
Release:	1
Summary:	Brazilian Portuguese female Kokoro voice pf_dora
URL:		https://huggingface.co/hexgrad/Kokoro-82M/tree/main/voices
License:	Apache-2.0
BuildArch:	noarch
Group:		System/Multimedia
Provides:	kokoro-voice
Provides:	kokoro-voice-pt
Provides:	kokoro-voice-pt_BR
Requires:	kokoro-model >= 1.0

%sourcelist
https://huggingface.co/hexgrad/Kokoro-82M/resolve/main/voices/pf_dora.pt

%description
%{summary}.
Uses the shared checkpoint in kokoro-model.
Pronunciation uses espeak-ng.
Select it with: kokoro -m pf_dora

%install
mkdir -p %{buildroot}%{_datadir}/kokoro/voices
install -c -m 644 %{S:0} %{buildroot}%{_datadir}/kokoro/voices/pf_dora.pt

%files
%{_datadir}/kokoro/voices/pf_dora.pt

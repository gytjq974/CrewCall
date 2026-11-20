# CrewCall 저장소의 코드 로드맵

이 저장소에서 실행되는 것은 AI가 읽는 Markdown 지침과 표시용 YAML이다. 행동을 바꾸려면 실행 패키지에서 해당 판단을 내리는 절을 찾고, 그 판단을 관찰할 평가 사례를 함께 읽는다. 이 로드맵은 CrewCall 자체를 개발하는 사람과 AI가 공유한다.

## 어디부터 읽을까?

| 담당할 일 | 첫 파일 | 다음에 확인할 곳 |
|---|---|---|
| 새 작업 시작, 작업 범위와 승인 시점 판단 | [SKILL.md](../../skills/crewcall/SKILL.md)의 ‘작업 경로와 승인’ | 이 저장소를 수정할 때 적용되는 [AGENTS.md](../../AGENTS.md), 이전 작업의 [현재 상태](current.md). E-20·E-21은 단순 작업과 기존 담당자 재사용 판단을 다룬다. |
| 기획의 실현 가능성 조사와 설계 | [기획·설계 지침](../../skills/crewcall/references/planning.md) | [코드 로드맵 작성 지침](../../skills/crewcall/references/code-map.md), [작업별 기획서와 설계서 저장 규칙](../../skills/crewcall/references/project-state.md) |
| 대상 프로젝트의 DB 구조를 기록하고 검증하는 방식 수정 | [데이터베이스 DDL 지침](../../skills/crewcall/references/database-schema.md) | [행동 평가 사례](../../evals/scenarios.md)의 E-12에서 실제 구조와 기록을 대조한다. |
| 스킬 동작 수정과 역할 인계 | 공통 행동은 [SKILL.md](../../skills/crewcall/SKILL.md), 담당자 간 전달은 [협업 지침](../../skills/crewcall/references/collaboration.md) | 버그를 다루는 방식은 [결함 조사](../../skills/crewcall/references/debugging.md), 테스트 범위와 완료 판단은 [검증 지침](../../skills/crewcall/references/verification.md) |
| 테스트와 독립 검토 | [행동 평가 사례](../../evals/scenarios.md)의 해당 요청과 판정 기준. E-22~E-25는 탐색 범위·DB 검증·검사 재사용·성능·인계 기록을 다룬다. | [개발 기록](../development.md)에 형식 검사 명령, 실제 행동 시험의 입력과 결과가 있다. 최초 프롬프트 변환의 정적 대조는 [0.9.1 검증 기록](../crewcall-0.9.1-verification.md)에 있다. |
| 사용자가 결과를 직접 확인하거나 개발 중 기획을 바꾸는 시점 | [사용자 실행 확인](../../skills/crewcall/references/verification.md#사용자가-직접-실행해-결과를-확인한다) · [개발 중 기획 변경](../../skills/crewcall/references/planning.md#개발-중-기획이-바뀌면) | E-17·E-18에서 대기, 변경 반영과 구현 재개를 확인한다. |
| 최종 구조 점검, 한글 주석과 파일 배치 규칙 수정 | [리팩토링 지침](../../skills/crewcall/references/refactoring.md) · [개발 환경별 디렉터리 규칙](../../skills/crewcall/references/project-layout.md) | E-13~E-15에서 중복·회귀·모듈별 배치 판단을, E-19에서 간결한 한글 주석과 완료 판단을 확인한다. |
| 사용 안내나 화면에 표시할 문구 수정 | 사용법은 [README](../../README.md), 이름·소개·시작 문구는 [openai.yaml](../../skills/crewcall/agents/openai.yaml) | 사용자에게 설명한 행동과 실제 스킬의 판단이 같은지 SKILL.md에서 확인한다. |

## 요청이 처리되는 흐름

사용자 요청 → 메인이 SKILL.md로 허용 범위와 진행 방법을 결정 → 해당 주제의 참조 문서를 읽음 → 대상 프로젝트에서 작업하고 확인 → 진행 상태와 결과를 기록한다. 예를 들어 설계 지침을 바꿀 때는 다음 세 지점을 따라간다.

1. **입력**은 사용자가 확정한 요구와 현재 작업의 기획서다. 작업별 파일은 `docs/workflow/tasks/<작업명>/`에 둔다. [로드맵 도입 기획서](tasks/design-feasibility/plan.md)
2. **판단**은 planning.md가 담당한다. 메인이 코드 로드맵에서 관련 위치를 찾고 원문을 확인한다. 다른 담당자의 조사가 필요하면 collaboration.md에 따라 질문과 확인할 파일을 보낸다.
3. **결과**는 해당 작업의 설계서와 current.md에 남긴다. 검토·구현·테스트 담당자는 그 자료로 작업 대상을 찾는다. [로드맵 도입 설계서](tasks/design-feasibility/design.md)

## 무엇을 확인했나?

2026-11-20 기준, Git HEAD `3ff016c` 위의 **미커밋 작업 폴더**를 확인했다. `rg --files`로 저장소의 주요 파일을 찾고 실행 패키지의 진입점, 참조 문서, YAML 설정, 평가 사례, 개발 기록을 대조했다. 임시 실습 프로젝트는 점검 범위에서 제외했다. 설치한 스킬이 자동으로 발견되는지는 별도 실환경 평가 항목이다.

다음 작업에서는 [개발 기록의 기본 검사 명령](../development.md#기본-검사)으로 스킬 형식을 확인한다. 행동이 달라졌다면 evals/scenarios.md에서 관련 사례를 실행한다. 새 파일이나 책임 이동이 생겼을 때 해당 행과 검증 경로만 고치고, 실행 결과는 개발 기록에 남긴다.

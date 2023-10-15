from typing import Dict, List

from chat import Chat
from classify_entity import ClassifyEntity
from classify_entity.entity import Entity

from .constants import DB_DIR, DOCS_DIR, ENTITY_JSON_PATH, FLAGS_JSON_PATH, URLS


class Alex:
    """ """

    _entity: Entity
    _chat: Chat
    _classifier: ClassifyEntity

    def __init__(self):
        """ """
        self._chat = Chat(docs_dir=DOCS_DIR, db_dir=DB_DIR, urls=URLS)
        self._classifier = ClassifyEntity(
            entities_json_path=ENTITY_JSON_PATH,
            flags_json_path=FLAGS_JSON_PATH,
            docs_dir=DOCS_DIR,
        )

    def chat(self, prompt: str) -> str:
        """ """
        return self._chat.chat(prompt)

    def update_flags(self, setup_answers: Dict[str, Dict]) -> List[str]:
        """ """
        result_flags = []

        def check_flag(flag_details: Dict) -> None:
            if flag_details.get("answer") == 1:
                result_flags.append(flag)

            for followup in flag_details.get("followups", []):
                for dep_flag, dep_details in followup.items():
                    check_flag(dep_details)

        for flag, details in setup_answers.items():
            check_flag(details)

        self._classifier.input_flags = result_flags
        return result_flags

    def entities_scores(self):
        """ """
        sorted_entities = self._classifier.entities
        scores = list(self._classifier.similarities)
        return list(zip(sorted_entities, scores))

    @property
    def setup_questions(self) -> Dict[str, Dict]:
        """ """
        flags = self._classifier.flags
        questions = {}
        for flag in flags:
            if flag.deps != []:
                continue
            questions[flag.mnemonic] = {
                "question": flag.question,
                "answer": 0,
                "followups": [],
            }
        for flag in flags:
            if flag.deps != []:
                continue
            for dep in flag.deps:
                questions[dep].get("followups").append(
                    {
                        flag.mnemonic: {
                            "question": flag.question,
                            "answer": 0,
                            "followups": [],
                        }
                    }
                )
        return questions

    @property
    def entity(self) -> Entity:
        """ """
        return self._entity

    @entity.setter
    def entity(self, entity: Entity) -> None:
        """ """
        self._entity = entity

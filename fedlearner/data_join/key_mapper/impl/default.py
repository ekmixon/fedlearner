from fedlearner.data_join.key_mapper.key_mapping import BaseKeyMapper
class DefaultKeyMapper(BaseKeyMapper):
    def leader_mapping(self, item) -> dict:
        return {}

    def follower_mapping(self, item) -> dict:
        return {}

    @classmethod
    def name(cls):
        return "DEFAULT"

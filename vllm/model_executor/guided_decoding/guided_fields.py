# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: Copyright contributors to the vLLM project

from dataclasses import dataclass
from typing import Optional, TypedDict, Union


# These classes are deprecated, see SamplingParams
class LLMGuidedOptions(TypedDict, total=False):
    guided_json: Union[dict, str]
    guided_regex: str
    guided_choice: list[str]
    guided_grammar: str
    guided_decoding_backend: str
    guided_whitespace_pattern: str
    guided_json_object: bool


@dataclass
class GuidedDecodingRequest:
    """One of the fields will be used to retrieve the logit processor."""
    guided_json: Optional[Union[dict, str]] = None
    guided_regex: Optional[str] = None
    guided_choice: Optional[list[str]] = None
    guided_grammar: Optional[str] = None
    guided_decoding_backend: Optional[str] = None
    guided_whitespace_pattern: Optional[str] = None
    guided_json_object: Optional[bool] = None
    structural_tag: Optional[str] = None

    def __post_init__(self):
        """Validate that some fields are mutually exclusive."""
        guide_count = sum(x is not None
                          for x in (self.guided_json, self.guided_regex,
                                    self.guided_choice, self.guided_grammar,
                                    self.guided_json_object,
                                    self.structural_tag))
        if guide_count > 1:
            raise ValueError(
                "You can only use one kind of guided decoding but multiple are "
                f"specified: {self.__dict__}")

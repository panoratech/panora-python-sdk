"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from panora import utils
from panora._hooks import AfterErrorContext, AfterSuccessContext, BeforeRequestContext, HookContext
from panora.models import components, errors, operations
from typing import List, Optional

class AtsScreeningquestion:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def get_screening_questions(self, x_connection_token: str, remote_data: Optional[bool] = None) -> operations.GetScreeningQuestionsResponse:
        r"""List a batch of ScreeningQuestions"""
        hook_ctx = HookContext(operation_id='getScreeningQuestions', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetScreeningQuestionsRequest(
            x_connection_token=x_connection_token,
            remote_data=remote_data,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/ats/screeningquestion'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        query_params = { **utils.get_query_params(request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetScreeningQuestionsResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScreeningQuestionsResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def add_screening_question(self, x_connection_token: str, unified_screening_question_input: components.UnifiedScreeningQuestionInput, remote_data: Optional[bool] = None) -> operations.AddScreeningQuestionResponse:
        r"""Create a ScreeningQuestion
        Create a screeningquestion in any supported Ats software
        """
        hook_ctx = HookContext(operation_id='addScreeningQuestion', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.AddScreeningQuestionRequest(
            x_connection_token=x_connection_token,
            remote_data=remote_data,
            unified_screening_question_input=unified_screening_question_input,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/ats/screeningquestion'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.AddScreeningQuestionRequest, "unified_screening_question_input", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = { **utils.get_query_params(request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.AddScreeningQuestionResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.AddScreeningQuestionResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[components.UnifiedScreeningQuestionOutput])
                res.unified_screening_question_output = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_screening_question(self, id: str, remote_data: Optional[bool] = None) -> operations.GetScreeningQuestionResponse:
        r"""Retrieve a ScreeningQuestion
        Retrieve a screeningquestion from any connected Ats software
        """
        hook_ctx = HookContext(operation_id='getScreeningQuestion', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetScreeningQuestionRequest(
            id=id,
            remote_data=remote_data,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(base_url, '/ats/screeningquestion/{id}', request)
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        query_params = { **utils.get_query_params(request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('GET', url, params=query_params, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.GetScreeningQuestionResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetScreeningQuestionResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def add_screening_questions(self, connection_token: str, x_connection_token: str, request_body: List[components.UnifiedScreeningQuestionInput], remote_data: Optional[bool] = None) -> operations.AddScreeningQuestionsResponse:
        r"""Add a batch of ScreeningQuestions"""
        hook_ctx = HookContext(operation_id='addScreeningQuestions', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.AddScreeningQuestionsRequest(
            connection_token=connection_token,
            remote_data=remote_data,
            x_connection_token=x_connection_token,
            request_body=request_body,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/ats/screeningquestion/batch'
        
        if callable(self.sdk_configuration.security):
            headers, query_params = utils.get_security(self.sdk_configuration.security())
        else:
            headers, query_params = utils.get_security(self.sdk_configuration.security)
        
        headers = { **utils.get_headers(request), **headers }
        req_content_type, data, form = utils.serialize_request_body(request, operations.AddScreeningQuestionsRequest, "request_body", False, False, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = { **utils.get_query_params(request), **query_params }
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        client = self.sdk_configuration.client
        
        try:
            req = client.prepare_request(requests_http.Request('POST', url, params=query_params, data=data, files=form, headers=headers))
            req = self.sdk_configuration.get_hooks().before_request(BeforeRequestContext(hook_ctx), req)
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), None, e)
            if e is not None:
                raise e

        if utils.match_status_codes(['4XX','5XX'], http_res.status_code):
            result, e = self.sdk_configuration.get_hooks().after_error(AfterErrorContext(hook_ctx), http_res, None)
            if e is not None:
                raise e
            if result is not None:
                http_res = result
        else:
            http_res = self.sdk_configuration.get_hooks().after_success(AfterSuccessContext(hook_ctx), http_res)
            
        
        
        res = operations.AddScreeningQuestionsResponse(http_meta=components.HTTPMetadata(request=req, response=http_res))
        
        if http_res.status_code == 200:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[operations.AddScreeningQuestionsResponseBody])
                res.object = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 201:
            # pylint: disable=no-else-return
            if utils.match_content_type(http_res.headers.get('Content-Type') or '', 'application/json'):                
                out = utils.unmarshal_json(http_res.text, Optional[List[components.UnifiedScreeningQuestionOutput]])
                res.unified_screening_question_outputs = out
            else:
                content_type = http_res.headers.get('Content-Type')
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)
        else:
            raise errors.SDKError('unknown status code received', http_res.status_code, http_res.text, http_res)

        return res

    

